from django.contrib.auth import authenticate
from django_ratelimit.decorators import ratelimit
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from datetime import timedelta
import pyotp
from ..models import OTP
import datetime

class CustomAuthView(APIView):
    permission_classes = [AllowAny]

    @ratelimit(key='ip', rate='5/5s', method='POST', block=True)
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            # Générer un OTP
            totp = pyotp.TOTP(user.username, interval=300)
            otp_code = totp.now()

            # Enregistrer l'OTP en base de données
            otp = OTP.objects.create(
                user=user,
                code=otp_code,
                expires_at=timezone.now() + timedelta(minutes=5)
            )

            user.profile.otp_code = otp_code 
            user.profile.otp_timestamp = datetime.datetime.now()
            user.profile.save()

            return Response({'message': 'OTP envoyé. Veuillez vérifier vos emails.', 'otp': f'{otp}'}, status=status.HTTP_200_OK)
        
        return Response({'error': 'Identifiants invalides'}, status=status.HTTP_401_UNAUTHORIZED)

    def handle_exception(self, exc):
        if isinstance(exc):
            return Response(
                {'error': 'Trop de tentatives, veuillez réessayer plus tard.'},
                status=429
            )
        return super().handle_exception(exc)
