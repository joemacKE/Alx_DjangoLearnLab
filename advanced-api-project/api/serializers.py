from .models import (Book, Author)
from .serializers import serializers
from datetime import timezone

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    publication_year = serializers.IntegerField()

    def get_publication_year(self):
        ...



#api/serializers.py doesn't contain: 
# ["class BookSerializer(serializers.ModelSerializer)", "serializers.ValidationError"]