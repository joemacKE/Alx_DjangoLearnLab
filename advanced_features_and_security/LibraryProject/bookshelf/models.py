from django.db import models
from django.contrib.auth.models import User, AbstractUser

class CustomeUser(AbstractUser):
    date_of_bith = models.DateTimeField()
    profile_photo = models.ImageField(upload_to='profile_pic/')



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=0000)

    def __str__(self):
        return self.title
# Create your models here.
#LibraryProject/bookshelf/models.py 
# doesn't contain: ["class CustomUser(AbstractUser):", "date_of_birth", 
# "profile_photo"]