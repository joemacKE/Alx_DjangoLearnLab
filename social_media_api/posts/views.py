from django.shortcuts import render
from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status

class PostListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        #this function retrieves all posts
        try:
            posts = Post.objects.all()
        except Post.DoesNotExist:
            return Response({'error': 'This post cannot be found'}, status=status.HTTP_404_NOT_FOUND)
        
        #serializes the post
        serialize = PostSerializer(posts, many=True)
        return Response(PostSerializer.data, status=status.HTTP_200_OK)
    
        


class CommentListAPIView(APIView):
    authentication_classes = [IsAuthenticated]
    permission_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request):
            #this function retrieves all posts
            try:
                posts = Post.objects.all()
            except Post.DoesNotExist:
                return Response({'error': 'This post cannot be found'}, status=status.HTTP_404_NOT_FOUND)
            
            #serializes the post
            serialize = PostSerializer(posts, many=True)
            return Response(PostSerializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"Post saved succesfully"}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors)



class PostDetailAPIView(APIView):
    ...


# Create your views here.
