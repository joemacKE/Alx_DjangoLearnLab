from .views import views, list_books, LibraryDetailView
from django.urls import path

urlpatterns = [
    path('list_books/', views.list_books.as_view(), name='list_books' ),
    path('login/', views.login.as_view(), name='login'),
    path('register/', views.register.as_view(), name='register'),
    path('logout/', views.logout.as_view(), name='logout' ),
]

#LibraryProject/relationship_app/urls.py 
# doesn't contain: ["from .views import list_books", "LibraryDetailView"]