from .models import (Author, Book)
from serializers import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
    
    class AuthorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Author
            fields = "__all__"