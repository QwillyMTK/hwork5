from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login
from .serializers import RegisterSerializer, LoginSerializer, ConfirmSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .tokens import CustomTokenObtainPairSerializer
from .utils import check_confirmation_code   # импортируем работу с Redis
from .models import CustomUser


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response({"message": "Успешный вход!"}, status=status.HTTP_200_OK)


class ConfirmView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        code = request.data.get("code")

        if check_confirmation_code(user_id, code):
            user = CustomUser.objects.get(id=user_id)
            user.is_active = True
            user.save()
            return Response({"message": "Аккаунт подтверждён!"}, status=status.HTTP_200_OK)

        return Response({"message": "Неверный или просроченный код"}, status=status.HTTP_400_BAD_REQUEST)


# JWT токен с birthdate
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
