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

    
    def test_about_view(self):
        """
        Test the about view.
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about-us.html')
        self.assertIn("about", response.context)
        self.assertIn("site_info", response.context)
