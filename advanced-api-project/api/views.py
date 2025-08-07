from rest_framework import generics
from api.serializers import BookSerializer, AuthorSerializer
from api.models import Book, Author

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer






# api/views.py doesn't contain:
#  ["DetailView", "CreateView", "UpdateView", "DeleteView"]
