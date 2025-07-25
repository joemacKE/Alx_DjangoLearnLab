
from django.shortcuts import render, redirect
from relationship_app.forms import BookForm
from .forms import ExampleForm
from django.contrib.auth.decorators import permission_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission

# Permission required: can_create = bookshelf | book | Can create
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



# - LibraryProject/bookshelf/views.py doesn't contain: 
# ["from .forms import ExampleForm"]