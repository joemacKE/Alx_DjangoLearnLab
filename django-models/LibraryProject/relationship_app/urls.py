from .views import views, list_books, LibraryDetailView
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('list_books/', views.list_books.as_view(), name='list_books' ),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('register/', views.register.as_view(), name='register'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout' ),
]

#LibraryProject/relationship_app/urls.py 
# doesn't contain: ["LogoutView.as_view(template_name=", "LoginView.as_view(template_name="]