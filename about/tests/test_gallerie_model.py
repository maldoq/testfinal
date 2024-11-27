from django.test import TestCase
from about.models import Gallerie
from tinymce.models import HTMLField
from datetime import datetime

class TestGallerieModel(TestCase):

    def test_gallerie_model(self):
        gallerie = Gallerie.objects.create(
            gallerie='gallerie/image/test_image.jpg',
            titre='Test Gallery',
            status=True
        )
        self.assertEqual(str(gallerie), 'Test Gallery')
        self.assertTrue(gallerie.status)
