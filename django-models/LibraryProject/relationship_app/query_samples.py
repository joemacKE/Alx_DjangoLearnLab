from .models import Author, Book, Library, Librarian

books = Book.objects.all()

books = Book.objects.prefetch_related(author='name')

librarian = Librarian.objects.get(name='library_name')



