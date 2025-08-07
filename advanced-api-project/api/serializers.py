from .models import (Book, Author)
from .serializers import serializers
from django.utils import timezone




class BookSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=255)
    publication_year = serializers.IntegerField()


    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value['publication_year'] > current_year:
            raise serializers.ValidationError(f"Publication year cannot be in the future")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Author
        fields = "__all__"


#api/serializers.py doesn't contain: ["serializers.ValidationError"]