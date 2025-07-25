from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.decorators import permission_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profile_pic/')

class CustomUserManager(BaseUserManager):
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
    class Meta:
        permissions = [
            ('can_view', 'Can view'),
            ('can_create', 'Can create'),
            ('can_edit', 'Can edit'),
            ('can_delete', 'Can delete')
        ]

class Command(BaseCommand):
    help = 'Create default groups and assign permissionss'

    def handle(self, *args, **kwargs):
        #editor group
        editor_group, _ = Group.objects.get_or_create(name="Editor")
        permissions = Permission.objects.filter(content_type=ContentType.objects.get_for_model(Book), codename_in=[
            'can_edit', 'can_create'

        ])
        editor_group.permissions.set(permissions)

        #viewers group
        viewer_group, _ = Group.objects.get_or_create(name='Viewer')
        permissions = Permission.objects.filter(content_type=ContentType.objects.get_for_model(Book), codename_in=[
            'can_view'
        ])
        viewer_group.permissions.set(permissions)

        #admin view group
        admin_group, _ = Group.objects.get_or_create(name='Admin')
        permissions = Permission.objects.filter(Content_type=ContentType.objects.get_for_model(Book), codename_in=[
            'can_add', 'can_view', 'can_create', 'can_delete'
        ])
        admin_group.permissions.set(permissions)
# Create your models here.
