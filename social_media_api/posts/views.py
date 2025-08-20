from posts.models import Post, Comment, Like
from notifications.models import Notification
from posts.serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions


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

class FeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        following_users = request.user.following.all()

        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def get(self, request, pk):
        try:
            post = generics.get_object_or_404(Post, pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'The post cannot be found'}, status=status.HTTP_404_NOT_FOUND)
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({'error': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)
        like = Like.objects.get_or_create(user=request.user, post=post)

        #this section creates a notification for post author
        if post.author != request.user:
            Notification.objects.create(
                recipient = post.author,
                actor = request.user,
                verb = 'liked your post',
                target = post
            )
        return Response({'message':'Post liked succesfully'}, status=status.HTTP_201_CREATED)
    


#posts/views.py doesn't contain: 
# ["generics.get_object_or_404(Post, pk=pk)", 
# "Like.objects.get_or_create(user=request.user, post=post)", "Notification.objects.create"]