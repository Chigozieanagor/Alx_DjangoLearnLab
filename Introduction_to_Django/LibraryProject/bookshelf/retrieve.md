book = Book.objects.all()
for bok in book:
     print(f"Title:{bok.title}, Author: {bok.author}, Year: {bok.publication_year}")   

#Title:1984, Author: George Orwell, Year: 1949

retrieve 
Book.objects.all()
#<QuerySet [<Book: Book object (1)>]>

