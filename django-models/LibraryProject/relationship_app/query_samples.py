from .models import Author, Book, Library, Librarian


def list_all_books(author):
    try:
        books = Book.objects.filter(author=author)
        return author.books
    except Author.DoesNotExist:
        return []

def librarian_for_a_library(librarian):
    try:
        librarian = Library.objects.get(library=librarian)
        return Library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None
    
    #LibraryProject/relationship_app/query_samples.py 
    # doesn't contain: ["Librarian.objects.get(library="]


def all_books(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library_name.books.all()
    except Library.DoesNotExist:
        return []

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None










