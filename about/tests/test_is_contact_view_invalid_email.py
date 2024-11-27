from django.test import TestCase, Client
from django.urls import reverse
from about.models import Contact, Presentation, Curriculum
from website.models import SiteInfo
from django.core.exceptions import ValidationError

class ViewsTestCase(TestCase):
    def setUp(self):
        """
        Set up initial data for testing.
        """
        # Adjusted SiteInfo creation
        self.site_info = SiteInfo.objects.create(
            email="test@example.com",
            nom="Test Site",
            telephone="1234567890",
            description="A test description",
            logo="test_logo.png",
            status=True,
        )
        
        # Create a dummy Presentation
        self.presentation = Presentation.objects.create(
            titre="About Us",
            description="Test description",
            image="test_image.jpg",
            status=True,
        )
        
        # Create a dummy Curriculum
        self.curriculum = Curriculum.objects.create(
            photo="test_photo.jpg",
            nom="John Doe",
            description="Test curriculum",
            cv="test_cv.pdf",
            status=True,
        )
        
        # Initialize the test client
        self.client = Client()

    def test_is_contact_view_invalid_email(self):
            """
            Test the is_contact view with invalid email.
            """
            invalid_data = {
                "name": "Test User",
                "email": "",
                "subject": "Test Subject",
                "tel": "1234567890",
                "messages": "Test Message",
            }
            response = self.client.post(reverse('is_contact'), data=invalid_data)
            self.assertEqual(response.status_code, 200)
            response_data = response.json()
            self.assertFalse(response_data.get("success"))
            self.assertEqual(response_data.get("message"), "email incorrect")