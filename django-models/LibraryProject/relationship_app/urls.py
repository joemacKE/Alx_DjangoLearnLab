from .views import views, list_books, LibraryDetailView
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view


urlpatterns = [
    path('list_books/', views.list_books.as_view(), name='list_books' ),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('register/', views.register.as_view(), name='register'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout' ),
    path('admin-view/', admin_view, name='admin-view'),
    path('librarian-view/', librarian_view, Name='librarian-view'),
    path('member-view/', member_view, name='member-view')
]

