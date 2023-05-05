from django.shortcuts import render

from books.models import Book


def book_list(request):
    books = Book.objects.all()[:1_000]
    return render(request, 'books/book_list.html', {'books': books})
