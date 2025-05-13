from django.shortcuts import render
from portal.models.book import Book

def catalog(request):
    books = Book.objects.all()
    return render(request, 'book/catalog.html', {'books': books})
