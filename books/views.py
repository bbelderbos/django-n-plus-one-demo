from django.shortcuts import render

from books.models import Book


def book_list(request):
    books = Book.objects.select_related("author")[:1_000]
    return render(request, 'books/book_list.html', {'books': books})
