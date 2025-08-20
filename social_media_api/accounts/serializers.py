from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

CustomUser = get_user_model
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only =True, required=True, validators=[validate_password])
    profile_picture = serializers.ImageField(required = False)

    class Meta:
        model = CustomUser
        fields = "__all__"

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
            bio = validated_data['bio'],
            profile_picture = validated_data['profile_picture'],
            followers = validated_data['followers']
        )
        return user
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()
        return instance

