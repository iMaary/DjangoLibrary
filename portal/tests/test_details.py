from django.test import TestCase
from django.urls import reverse
from portal.models.book import Book

class DetailsViewTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test Description",
            publication_date="2023-05-01"
        )

    def test_details_view_status_code(self):
        url = reverse('details', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)

    def test_details_view_template(self):
        url = reverse('details', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        
        self.assertTemplateUsed(response, 'book/details.html')
