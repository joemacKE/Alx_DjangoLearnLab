from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from accounts.models import CustomUser


class FollowUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, user_id):
        users = CustomUser.objects.all()
        user_to_follow = get_object_or_404(CustomUser, id =user_id)

        if request.user == user_to_follow:
            return Response({'error':"You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({'message': f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)


class UnfollowAUserPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        #current user unfollows another user
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

        if request.user == user_to_unfollow:
            return Response({'error':'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(user_to_unfollow)
        return Response({'message': f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)

class FollowersListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        """Get list of followers for a user"""
        user = get_object_or_404(CustomUser, id=user_id)
        followers = user.followers.all().values("id", "username", "email")
        return Response(followers, status=status.HTTP_200_OK)

class FollowingListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        """Get list of users that this user follows"""
        user = get_object_or_404(CustomUser, id=user_id)
        following = user.following.all().values("id", "username", "email")
        return Response(following, status=status.HTTP_200_OK)

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
# accounts/views.py doesn't contain: ["CustomUser.objects.all()"]
