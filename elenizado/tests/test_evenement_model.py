from django.test import TestCase
from django.urls import reverse
from elenizado.models import Categorie, Publication, Commentaire, ReponseCommentaire, Like, Evenement, Cours, Textes, Video
from django.utils.text import slugify
from datetime import datetime

class EvenementModelTest(TestCase):

    def test_evenement_creation(self):
        evenement = Evenement.objects.create(
            titre='Annual Tech Conference',
            description='A conference on the latest tech trends'
        )
        self.assertEqual(evenement.titre, 'Annual Tech Conference')
        self.assertTrue(evenement.status)

    def test_evenement_slug_creation(self):
        evenement = Evenement.objects.create(
            titre='Annual Tech Conference',
            description='A conference on the latest tech trends'
        )
        self.assertIsNotNone(evenement.slug)

    def test_evenement_str(self):
        evenement = Evenement.objects.create(
            titre='Annual Tech Conference',
            description='A conference on the latest tech trends'
        )
        self.assertEqual(str(evenement), 'Annual Tech Conference')