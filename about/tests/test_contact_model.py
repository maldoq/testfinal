from django.test import TestCase
from about.models import Contact
from tinymce.models import HTMLField
from datetime import datetime

class TestContactModel(TestCase):

    def test_contact_model(self):
        contact = Contact.objects.create(
            nom='Test User',
            email='testuser@example.com',
            subject='Test Subject',
            telephone=123456789,
            message='This is a test message',
            status=True
        )
        self.assertEqual(str(contact), 'Test User')
        self.assertEqual(contact.email, 'testuser@example.com')
        self.assertEqual(contact.subject, 'Test Subject')