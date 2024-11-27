from django.test import TestCase
from django.urls import reverse
from elenizado.models import Categorie, Publication, Commentaire, ReponseCommentaire, Like, Evenement, Cours, Textes, Video
from django.utils.text import slugify
from datetime import datetime

class CoursModelTest(TestCase):

    def test_cours_creation(self):
        cours = Cours.objects.create(
            titre='Django Basics',
            niveau='Beginner',
            annee=2024,
            description='Intro to Django framework'
        )
        self.assertEqual(cours.titre, 'Django Basics')
        self.assertEqual(cours.niveau, 'Beginner')
        self.assertEqual(cours.annee, 2024)

    def test_cours_str(self):
        cours = Cours.objects.create(
            titre='Django Basics',
            niveau='Beginner',
            annee=2024,
            description='Intro to Django framework'
        )
        self.assertEqual(str(cours), 'Django Basics')