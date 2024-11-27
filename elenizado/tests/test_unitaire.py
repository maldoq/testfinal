from datetime import datetime
from django.test import TestCase, Client
from django.urls import reverse
from elenizado.models import Publication, SiteInfo, Categorie
from elenizado import models
from about.models import Gallerie
from django.utils.text import slugify

class TimelineViewTest(TestCase):
    # Configuration du siteInfo
    def setUp(self):
        self.client = Client()
        self.site_info = SiteInfo.objects.create(
            email="test@example.com",
            nom="Test Site",
            telephone="1234567890",
            description="A test description",
            logo="test_logo.png",
            status=True,
        )
    
    # Voir si la page d'accueil répond donc est accéssible
    def test_timeline_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

class DetailViewTest(TestCase):
    # Configuration du siteInfo et d'une publivation avec une categorie donnée
    def setUp(self):
        self.client = Client()
        self.site_info = SiteInfo.objects.create(
            email="testq@example.com",
            nom="Test Site",
            telephone="123456788",  
            description="Test description",
            logo="test_logo.png",  
            status=True
        )
        self.categorie = Categorie.objects.create(
            nom='Technology',
            description='Category for tech publications'
        )
        self.publication = Publication.objects.create(
            titre="Test Publication",
            image="images/logo.png",
            description='This is a test post for Django testing',
            categorie=self.categorie,
            status=True
        )

    def test_detail_view(self):
        slug = '-'.join((slugify(self.publication.titre), slugify(datetime.now().microsecond)))
        response = self.client.get(reverse('detail', args=[slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/detail-standart.html')
        self.assertEqual(response.context['publication'], self.publication)
        self.assertTrue(self.publication.slug.startswith(slug))


class CoursViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.site_info = SiteInfo.objects.create(
            email="test@example.com",
            nom="Test Site",
            telephone="123456791",  
            description="AA Test description",
            logo="test_logo.png",  
            status=True
        )
        self.course = models.Cours.objects.create(
            titre="Test Course", 
            annee=2024,
            description="Good course for you",
            image="images/logo.png",
            cours="cours/",
            status=True
        )

    def test_cours_view(self):
        response = self.client.get(reverse('cours'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/cours.html')
        self.assertIn('cours', response.context)

class VideoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.site_info = SiteInfo.objects.create(
            email="test@example.com",
            nom="Test Site",
            telephone="123456792",  
            description="Ah ouais Test description",
            logo="test_logo.png",  
            status=True
        )
        self.video = models.Video.objects.create(
            titre="Test Video", 
            description="good video",
            image="images/video/video.png",
            video="https://www.youtube.com/watch?v=m25ppbdW5Kc",
            status=True
        )

    def test_video_view(self):
        response = self.client.get(reverse('video'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/video-custom-player.html')
        self.assertIn('video', response.context)

class IsCommentaireViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.categorie = Categorie.objects.create(
            nom='Technology',
            description='Category for tech publications'
        )
        self.publication = models.Publication.objects.create(
            titre="Test Publication", 
            categorie=self.categorie,
            status=True
        )

    def test_is_commentaire_valid(self):
        data = {
            'id': self.publication.id,
            'nom': 'Test User',
            'email': 'testuser@example.com',
            'commentaire': 'This is a test comment.'
        }
        response = self.client.post(reverse('is_commentaire'), data)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertTrue(response_data['success'])

class IsReponsesCommentairesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.categorie = Categorie.objects.create(
            nom='Technology',
            description='Category for tech publications'
        )
        self.publication = models.Publication.objects.create(
            titre="Test Publication", 
            categorie=self.categorie,
            status=True
        )
        self.comment = models.Commentaire.objects.create(
            publication=self.publication,
            nom="Test User", 
            email="test@example.com", 
            commentaire="Test comment."
        )

    def test_is_reponsescommentaires_valid(self):
        data = {
            'id_commentaire': self.comment.id,
            'name': 'Responder',
            'mail': 'responder@example.com',
            'reponsecommentaires': 'Test reply.'
        }
        response = self.client.post(reverse('is_reponsescommentaires'), data)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertTrue(response_data['success'])
