from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('librarian', 'Librarian'),
    ('member', 'Member')
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=120, choices=ROLE_CHOICES)

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name="library")

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=120)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
