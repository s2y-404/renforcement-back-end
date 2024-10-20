from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from ..models import OTP
import pyotp
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
import os

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            user = self.get_user(request.data['username'])
            
            if user:
                # Utilisation de l'ID de l'utilisateur pour générer un secret
                secret = pyotp.random_base32()
                totp = pyotp.TOTP(secret)
                otp_code = totp.now()
                
                # Définir l'expiration de l'OTP
                expires_at = timezone.now() + timedelta(minutes=5)

                # Enregistrer l'OTP dans la base de données
                OTP.objects.create(user=user, code=otp_code, expires_at=expires_at)

                # Envoyer l'OTP par email
                send_mail(
                    'Votre code OTP',
                    f'Voici votre code OTP : {otp_code}',
                    f'{os.getenv('EMAIL')}',
                    [user.email],
                    fail_silently=False,
                )

                return Response({'message': 'OTP envoyé. Veuillez vérifier votre email.'}, status=status.HTTP_200_OK)
        
        return response

    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None
