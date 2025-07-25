from django.core.management.base import BaseCommand
from django.shortcuts import render, redirect
from relationship_app.forms import BookForm
from .models import Book
from django.contrib.auth.decorators import permission_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission

@permission_required('bookshelf.permissions', raise_exception=True)
def can_view(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_list.html', {'form':form})


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

#@permission_required('bookshelf.permission', raise_exception=True)



# Create your views here.
#LibraryProject/bookshelf/views.py doesn't contain: ["book_list"]
