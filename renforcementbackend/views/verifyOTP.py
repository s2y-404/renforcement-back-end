from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from ..models import OTP

class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        otp_code = request.data.get("otp")

        try:
            user = User.objects.get(username=username)
            otp = OTP.objects.get(user=user, code=otp_code)

            if otp.is_expired():
                return Response({'error': 'Le code OTP a expiré.'}, status=status.HTTP_400_BAD_REQUEST)

            # Supprimer l'OTP après validation
            otp.delete()

            # Générer le token JWT
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        except OTP.DoesNotExist:
            return Response({'error': 'Code OTP invalide.'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'Utilisateur non trouvé.'}, status=status.HTTP_404_NOT_FOUND)
