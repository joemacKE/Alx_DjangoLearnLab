from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token

CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    following_count = serializers.IntegerField(source='following.count', read_only=True)
    model = CustomUser
    fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only =True, required=True, validators=[validate_password])
    # profile_picture = serializers.ImageField(upload_to='profile/', blank=True)
    
    class Meta:
        model = CustomUser
        fields = "__all__"


    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
            bio = validated_data['bio'],
            # profile_picture = validated_data['profile_picture'],

        )
        return user
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()
        return instance

#accounts/serializers.py doesn't contain: 
# ["from rest_framework.authtoken.models import Token", 
# "serializers.CharField()", "Token.objects.create", "get_user_model().objects.create_user"]