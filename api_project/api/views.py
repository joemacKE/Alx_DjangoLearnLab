from django.shortcuts import render, get_object_or_404
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import generics
from .models import Book
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# class BookList(generics.ListAPIView):
#     query_set = Book.objects.all()
#     serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        permission_classes = [IsAuthenticated]
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
