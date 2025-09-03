create
new_book = Book(title = '1984', author = 'George Orwell', publication_year = '1949')
new_book.save()
#


Retrieve
book = Book.objects.all()
for bok in book:
     print(f"Title:{bok.title}, Author: {bok.author}, Year: {bok.publication_year}")

#Title:1984, Author: George Orwell, Year: 1949

retrieve
Book.objects.all()
#<QuerySet [<Book: Book object (1)>]>


update
Book.objects.filter(title = '1984').update(title = 'Nineteen Eighty-Four')
#1

Delete
Book.objects.all().delete()
#(1, {'bookshelf.Book': 1})

Retrieve
book = Book.objects.all()
for bok in book:
     print(f"Title:{bok.title}, Author: {bok.author}, Year: {bok.publication_year}")

#Title:1984, Author: George Orwell, Year: 1949

retrieve
Book.objects.all()
#<QuerySet [<Book: Book object (1)>]>
