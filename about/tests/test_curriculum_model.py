from django.test import TestCase
from about.models import Curriculum
from tinymce.models import HTMLField
from datetime import datetime

class Test_curriculum_model(TestCase):

    def test_curriculum_model(self):
        curriculum = Curriculum.objects.create(
            photo='images/curriculum/test_photo.jpg',
            nom='Test Curriculum',
            description='<p>This is a test description</p>',
            cv='cv/curriculum/test_cv.pdf',
            status=True
        )
        self.assertEqual(str(curriculum), 'Test Curriculum')
        self.assertTrue(curriculum.status)