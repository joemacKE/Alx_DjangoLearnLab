from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import generics
from .models import Book


class BookList(generics.ListAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer


# Create your views here.
#api/views.py doesn't contain: 
# ["BookList", "generics.ListAPIView", 
# "from .serializers import BookSerializer"]