from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.response import Response
from user.serializers import CustomUserSerislizer, CustomUserLoginSerislizer
from user.models import CustomUser
# Create your views here.

class RegisterUserAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerislizer
    

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserLoginSerislizer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(request, username=username, password=password)


        if user:
            login(request, user)  
            return Response({
                'user_id': user.id,
                'username': user.username,
                'message': 'Login successful'
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_204_NO_CONTENT)
    





