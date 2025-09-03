from bookshelf.models import Book
book = Book.obejects.get(title = 'Ninteen Eighty-Four')
book.delete()
Book.objects.all().delete()
#(1, {'bookshelf.Book': 1})
