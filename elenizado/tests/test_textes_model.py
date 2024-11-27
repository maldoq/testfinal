from django.test import TestCase
from django.urls import reverse
from elenizado.models import Categorie, Publication, Commentaire, ReponseCommentaire, Like, Evenement, Cours, Textes, Video
from django.utils.text import slugify
from datetime import datetime

class TextesModelTest(TestCase):

    def test_textes_creation(self):
        texte = Textes.objects.create(
            titre='Learning Django',
            description='A comprehensive guide to Django',
            pdf='some/path/to/file.pdf'
        )
        self.assertEqual(texte.titre, 'Learning Django')

    def test_textes_str(self):
        texte = Textes.objects.create(
            titre='Learning Django',
            description='A comprehensive guide to Django',
            pdf='some/path/to/file.pdf'
        )
        self.assertEqual(str(texte), 'Learning Django')