from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Library, Book, Librarian, Author


def book_list(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class BookDetailView(DetailView):
    model = Library
    template_name = 'books/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context



# Create your views here.
#LibraryProject/relationship_app/views.py 
# doesn't contain: ["from django.views.generic.detail import DetailView"]