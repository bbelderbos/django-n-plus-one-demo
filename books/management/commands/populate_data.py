from django.core.management.base import BaseCommand

from books.models import Author, Book


class Command(BaseCommand):
    help = 'Populates the database with random data.'

    def handle(self, *args, **options):
        # Create 1000 authors
        authors = []
        for i in range(1000):
            author = Author(name=f'Author {i}')
            authors.append(author)

        Author.objects.bulk_create(authors)

        # Create 1000 books for each author
        books = []
        for author in authors:
            for i in range(1000):
                book = Book(title=f'Book {i}', author_id=author.id)
                books.append(book)

        Book.objects.bulk_create(books)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(authors)} authors and {len(books)} books.'))

