from posts.models import Post, Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at', 'author']

