from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from .models import Book, Library, Librarian, Author


def all_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, "books/list_books.html", context)

class BookDetailView(DetailView):
    model = Library
    template_name = 'library/library_detail.html'

    def books_in_library(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        


# Create your views here.
#LibraryProject/relationship_app/views.py 
# doesn't contain: ["relationship_app/list_books.html"]