from .models import Author, Book, Library, Librarian

books = Book.objects.prefetch_related(author='name')
librarian = Librarian.objects.all()