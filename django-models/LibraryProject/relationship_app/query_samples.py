from .models import Author, Book, Library, Librarian
books = Book.objects.filter(author__name  = 'author_name')
libraries = Library.objects.get(name=library_name) 
book1 = Library.books.all()
librarians = Librarian.objects.all()
