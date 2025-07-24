from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_pic/')

class CustomUserManager(BaseUserManager):
    pass


    #logic for creating a user
    def create_user(self, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        if not email:
            raise ValueError("User must have a valid email address")
        email = self.normalize_email(email),
        user = self.model(
            email = email,
            date_of_birth = date_of_birth,
            profile_photo = profile_photo
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    #creating a super user
    def create_superuser(self, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        if not email:
            raise ValueError("User must have a valid email address")
        user = self.model(
            email = self.normalize_email(email, password=password),
            date_of_birth = date_of_birth,
            profile_photo = profile_photo,
        )
        user.is_admin= True
        user.save(using=self._db)
        return user


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=0000)

    def __str__(self):
        return self.title
# Create your models here.
