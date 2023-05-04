import random

from django.core.management.base import BaseCommand

from books.models import Author, Book


class Command(BaseCommand):
    help = 'Populates the database with random data.'

    def handle(self, *args, **options):
        # Create 1000 authors
        authors = []
        for i in range(1000):
            author = Author.objects.create(name=f'Author {i}')
            authors.append(author)

        # Create 1000 books for each author
        books = []
        for author in authors:
            for i in range(1000):
                book = Book.objects.create(
                    title=f'Book {i}',
                    author=author,
                )
                books.append(book)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(authors)} authors and {len(books)} books.'))
