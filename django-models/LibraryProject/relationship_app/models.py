from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = 'books')
    def __init__(self, title, urls):
        self.title = title
        self.urls = urls
        

class Library(models.Model):
    name = models.CharField(max_length = 200)
    books = models.ManyToManyField(Book, related_name= 'Book')

class Librarian(models.Model):
    name = models.CharField(max_length = 200)
    library = models.OneToOneField(Library, on_delete = models.CASCADE)
