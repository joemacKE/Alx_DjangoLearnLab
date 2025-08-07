from rest_framework import generics
from api.serializers import BookSerializer, AuthorSerializer
from api.models import Book, Author

class ListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# Create your views here.
