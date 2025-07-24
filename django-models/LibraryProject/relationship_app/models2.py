from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User, AbstractUser

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile/')
    bio = models.TextField()
    phone_number = models.PositiveIntegerField(max_length=10)

    class Meta:
        permission = [
            ('can_delete_account', 'Can Delete Account'),
            ('')
        ]