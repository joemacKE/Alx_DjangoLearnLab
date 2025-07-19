from .views import views, list_books, LibraryDetailView
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view, add_book, edit_book, delete_book, book_list


urlpatterns = [
    path('list_books/', views.list_books.as_view(), name='list_books' ),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('register/', views.register.as_view(), name='register'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout' ),
    path('admin-view/', admin_view, name='admin-view'),
    path('librarian-view/', librarian_view, Name='librarian-view'),
    path('member-view/', member_view, name='member-view'),
    path('books/', book_list, name='book-list')
    path('books/add/', add_book, Name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit-book'),
    path('books/<int:pk>/delete', delete_book, name='delete-book')
]

