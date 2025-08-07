from rest_framework import generics
from api.serializers import BookSerializer, AuthorSerializer
from api.models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated 
from django_filters import rest_framework

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'publication_year']


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# api/views.py doesn't 
# contain: ["from rest_framework.permissions import 
# IsAuthenticatedOrReadOnly, IsAuthenticated", "IsAuthenticated"]
