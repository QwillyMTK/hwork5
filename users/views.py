from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login
from .serializers import RegisterSerializer, LoginSerializer, ConfirmSerializer


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
        serializer = ConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        user.is_active = True
        user.confirm_code = None
        user.save()
        return Response({"message": "Аккаунт подтверждён!"}, status=status.HTTP_200_OK)
