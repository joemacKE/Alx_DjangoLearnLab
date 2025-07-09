python manage.py shell
from bookshelf.models import Book
book = Book.objects.get(title = "Nineteen Eighty-Four")
book.delete()
print(book.objects.all())
#Expected output: <QuerySet []>
