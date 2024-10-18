from django.contrib.auth import authenticate
from django_ratelimit.decorators import ratelimit
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

class CustomAuthView(APIView):
    permission_classes = [AllowAny]

    @ratelimit(key='ip', rate='5/5s', method='POST', block=True)
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    def handle_exception(self, exc):
        if isinstance(exc):
            return Response(
                {'error': 'Trop de tentatives, veuillez réessayer plus tard.'},
                status=429
            )
        return super().handle_exception(exc)
