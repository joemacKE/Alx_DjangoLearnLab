from django.test import TestCase
from django.contrib.auth.models import User, Group

# Create test users
editor_user = User.objects.create_user(username='editor1', password='testpass123')
viewer_user = User.objects.create_user(username='viewer1', password='testpass123')
admin_user = User.objects.create_user(username='admin1', password='testpass123')

# Assign to groups
editor_group = Group.objects.get(name='Editor')
viewer_group = Group.objects.get(name='Viewer')
admin_group = Group.objects.get(name='Admin')

editor_user.groups.add(editor_group)
viewer_user.groups.add(viewer_group)
admin_user.groups.add(admin_group)


# Create your tests here.
