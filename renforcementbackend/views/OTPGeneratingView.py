from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from ..models import OTP
import pyotp
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

class OTPGeneratingView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            user = self.get_user(request.data['username'])
            
            if user:
                secret = pyotp.random_base32()
                totp = pyotp.TOTP(secret)
                otp_code = totp.now()
                expires_at = timezone.now() + timedelta(minutes=5)

                OTP.objects.create(user=user, code=otp_code, expires_at=expires_at)
            
                try:
                    send_mail(
                        'Votre code OTP',
                        f'Voici votre code OTP : {otp_code}',
                        f'{os.getenv('EMAIL_HOST_USER')}',
                        [user.email],
                        fail_silently=False,
                    )
                    return Response({'message': 'OTP envoyé. Veuillez vérifier votre email.'}, status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({"detail": f"Une erreur s'est produite lors de l'envoi de l'e-mail : {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


            return Response({"detail": "Identifiants incorrects"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return response

    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None
