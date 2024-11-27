from django.test import TestCase
from django.urls import reverse
from elenizado.models import Categorie, Publication, Commentaire, ReponseCommentaire, Like, Evenement, Cours, Textes, Video
from django.utils.text import slugify
from datetime import datetime

class CategorieModelTest(TestCase):

    # Création d'une categorie professeur
    def test_categorie_creation(self):
        categorie = Categorie.objects.create(
            nom='Professeur',
            description='publication de professeur'
        )
        self.assertEqual(categorie.nom, 'Professeur')
        self.assertEqual(categorie.description, 'publication de professeur')
        self.assertTrue(categorie.status)

    def test_categorie_str(self):
        categorie = Categorie.objects.create(nom='Music', description='Music related publications')
        self.assertEqual(str(categorie), 'Music')