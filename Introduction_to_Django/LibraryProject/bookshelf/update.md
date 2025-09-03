book = Book.objects.get(title = 1984)
book.title = 'Nineteen Eighty-Four'
book.save()
Book.objects.filter(title = '1984').update(title = 'Nineteen Eighty-Four')
#1
