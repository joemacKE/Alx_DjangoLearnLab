from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must provide a valid email address")
        extra_fields.setdefault('username', email)

        user = self.model(
            email = self.normalize_email(email), **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("You must provide a valid email")
        user = self.create_user(
            email = email,
            password = password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    email = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)


    def __str__(self):
        return self.username


# Create your models here.
