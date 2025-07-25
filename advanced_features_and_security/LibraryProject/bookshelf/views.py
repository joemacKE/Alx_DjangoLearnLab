
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



#@permission_required('bookshelf.permission', raise_exception=True)



# Create your views here.
#LibraryProject/bookshelf/views.py doesn't contain: ["book_list"]
