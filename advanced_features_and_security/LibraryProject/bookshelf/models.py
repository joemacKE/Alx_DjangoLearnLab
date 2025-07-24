from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class CustomUser(AbstractUser):
    date_of_bith = models.DateTimeField()
    profile_photo = models.ImageField(upload_to='profile_pic/')

class CustomUserManager(BaseUserManager):
    """This class handles the creation of users"""
    def create_user(self, email, password, **extra_fields):
        pass
    def create_superuser(self, email, password, **extra_fields):
        pass


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=0000)

    def __str__(self):
        return self.title
# Create your models here.
#LibraryProject/bookshelf/models.py doesn't contain: 
# ["class CustomUser(AbstractUser):", "date_of_birth"
#LibraryProject/bookshelf/models.py 
# - LibraryProject/bookshelf/models.py 
# doesn't contain: ["class CustomUserManager(BaseUserManager):", "create_user", 
# "create_superuser"]