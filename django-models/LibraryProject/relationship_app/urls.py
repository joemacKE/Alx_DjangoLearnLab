from .views import views, list_books, LibraryDetailView
from django.urls import path

urlpatterns = [
    path('list_books/', views.list_books.as_view(), name='list_books' )
]

#LibraryProject/relationship_app/urls.py 
# doesn't contain: ["from .views import list_books", "LibraryDetailView"]