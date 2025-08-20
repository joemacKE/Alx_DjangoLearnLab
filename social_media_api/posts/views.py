from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class PostListViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = []
class CommentListViewSet(viewsets.ViewSet):
    """
    Handles listing comments for a specific post
    and creating a comment under a post.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, post_pk=None):
        """Return all comments for a given post"""
        post = get_object_or_404(Post, pk=post_pk)
        serializer = PostSerializer(post)  # returns post + nested comments
        return Response(serializer.data)

    def create(self, request, post_pk=None):
        """Add a comment under a given post"""
        post = get_object_or_404(Post, pk=post_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post, user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)






#posts/views.py doesn't contain: ["viewsets.ModelViewSet", 
#posts/views.py doesn't contain: ["Comment.objects.all()"