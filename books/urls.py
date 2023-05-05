from django.urls import path

from books.views import book_list

app_name = 'books'
urlpatterns = [
    path('books/', book_list, name='book_list'),
]
