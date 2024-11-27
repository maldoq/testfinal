from django.test import TestCase
from about.models import Presentation
from tinymce.models import HTMLField
from datetime import datetime

class TestPresentationModel(TestCase):

    def test_presentation_model(self):
        presentation = Presentation.objects.create(
            titre='Test Presentation',
            image='image/presentation/test_image.jpg',
            description='<p>This is a test presentation description</p>',
            status=True
        )
        self.assertEqual(str(presentation), 'Test Presentation')
        self.assertTrue(presentation.status)