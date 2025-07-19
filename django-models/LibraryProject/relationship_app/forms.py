from .models import UserProfile, Author, Book, Library, Librarian
from django import forms



class LibrarianProfileForm(forms.ModelForm):
    class Meta:
        model = Librarian
        fields = ['name', 'library']

class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
    