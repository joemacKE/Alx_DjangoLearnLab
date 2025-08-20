from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterAPIView(APIView):
    myuser = get_user_model()
    permission_classes = [AllowAny]
    def post(self, request):
        #this will register a user
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"User registered succesfully"}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class LogOutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        #logging out a user
        try:
            refresh_token = request.data.get('refresh_toke')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message':"Logged out succesfully"})
        except Exception as e:
            return Response({'error':'Invalid token'})

# Create your views here.
