from .models import Author, Book, Library, Librarian

def all_books():
    books = Book.objects.all()
    return books.all()

def librarian():
    librarian = Library.objects.get(name='library_name')
    return librarian.books.all()

def book_by_authro():
    books_by_author = Book.objects.get(name='author')





