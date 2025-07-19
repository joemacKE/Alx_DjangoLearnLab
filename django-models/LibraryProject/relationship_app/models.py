from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('librarian', 'Librarian'),
    ('member', 'Member'),
]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=120, choices=ROLE_CHOICES)


    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    class Meta:
        permissions = [('can_add_book', 'Can add a book'),
                      ('can_change_book', 'Can change a book'),
                      ('can_delete_book', 'Can delete a book'),
                    ]


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
