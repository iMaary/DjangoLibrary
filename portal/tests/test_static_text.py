from django.test import TestCase
from portal.models import StaticText

class StaticTextModelTest(TestCase):

    def test_static_text_creation(self):
        static_text = StaticText.objects.create(
            key="homepage123_title",
            content="Welcome to the Library Portal!"
        )
        
        self.assertEqual(str(static_text), static_text.key)
        self.assertEqual(static_text.key, "homepage123_title")
        self.assertEqual(static_text.content, "Welcome to the Library Portal!")
