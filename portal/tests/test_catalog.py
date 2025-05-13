from django.test import TestCase
from django.urls import reverse
from portal.models.book import Book

class CatalogViewTest(TestCase):
    def setUp(self):
        Book.objects.create(
            title="Book 1",
            author="Author 1",
            description="Description 1",
            publication_date="2023-01-01"
        )
        Book.objects.create(
            title="Book 2",
            author="Author 2",
            description="Description 2",
            publication_date="2023-02-01"
        )

    def test_catalog_view_status_code(self):
        url = reverse('catalog')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        
    def test_catalog_view_template(self):
        url = reverse('catalog')
        response = self.client.get(url)
        
        self.assertTemplateUsed(response, 'book/catalog.html')
