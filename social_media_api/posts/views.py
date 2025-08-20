from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework import status, viewsets


class PostListViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_calsses = PostSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class CommentListViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]




#posts/views.py doesn't contain: ["viewsets.ModelViewSet", 
#posts/views.py doesn't contain: ["Comment.objects.all()"]