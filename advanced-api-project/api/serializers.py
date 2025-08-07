from .models import (Book, Author)
from .serializers import serializers
from datetime import timezone




class BookSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=255)
    publication_year = serializers.IntegerField()


    def get_publication_year(self):
        ...

class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Author
        fields = "__all__"


#api/serializers.py doesn't contain: ["(many=True, read_only=True)"]