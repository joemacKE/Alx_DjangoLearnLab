from .serializers import serializer
from .models import Book

class BookSerializer(serializer.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'