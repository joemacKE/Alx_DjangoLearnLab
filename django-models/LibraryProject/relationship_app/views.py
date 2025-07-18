from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from .models import Book, Library, Librarian, Author


def book_list(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, "books/list_books.html", context)




# Create your views here.
#LibraryProject/relationship_app/views.py 
# doesn't contain: ["relationship_app/library_detail.html", "from .models import Library"]