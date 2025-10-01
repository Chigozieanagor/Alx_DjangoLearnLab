from .models import Author, Book, Library, Librarian
books = Book.objects.filter(author__name  = 'author_name')
libraries = Library.objects.all()
librarians = Librarian.objects.all()
