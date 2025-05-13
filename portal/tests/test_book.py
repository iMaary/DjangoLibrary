from django.test import TestCase
from portal.models.book import Book

class BookModelTest(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(
            title="This is the name of the book",
            author="Jane Doe",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            publication_date="2023-01-01"
        )
        self.assertEqual(str(book), "This is the name of the book")
