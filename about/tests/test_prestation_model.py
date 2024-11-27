from django.test import TestCase
from about.models import Prestation
from tinymce.models import HTMLField
from datetime import datetime

class TestPrestationModel(TestCase):

    def test_prestation_model(self):
        prestation = Prestation.objects.create(
            titre='Test Prestation',
            description='This is a test prestation description',
            image='images/prestations/test_image.jpg',
            status=True
        )
        self.assertEqual(str(prestation), 'Test Prestation')
        self.assertTrue(prestation.status)