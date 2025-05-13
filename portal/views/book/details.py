from django.shortcuts import render, get_object_or_404
from portal.models.book import Book

def details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/details.html', {'book': book})
