from api.views import (
    BookListView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
    BookCreateView
    )
from urls import path

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name = 'book-create'),
    path('books/update/', BookUpdateView.as_view(), name="book-update"),
    path('books/delete/', BookDeleteView.as_view(), name = 'book-delete')
]

#api/urls.py doesn't contain: ["books", "books/create", "books/update", "books/delete"]