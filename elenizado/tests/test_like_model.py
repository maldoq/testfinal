from django.test import TestCase
from django.urls import reverse
from elenizado.models import Categorie, Publication, Commentaire, ReponseCommentaire, Like, Evenement, Cours, Textes, Video
from django.utils.text import slugify
from datetime import datetime

class LikeModelTest(TestCase):

    def test_like_creation(self):
        categorie = Categorie.objects.create(
            nom='Technology',
            description='Category for tech publications'
        )
        publication = Publication.objects.create(
            titre='Django Testing',
            description='This is a test post for Django testing',
            categorie=categorie
        )
        like = Like.objects.create(publication=publication)
        self.assertEqual(like.publication.titre, 'Django Testing')

    def test_like_str(self):
        categorie = Categorie.objects.create(
            nom='Technology',
            description='Category for tech publications'
        )
        publication = Publication.objects.create(
            titre='Django Testing',
            description='This is a test post for Django testing',
            categorie=categorie
        )
        like = Like.objects.create(publication=publication)
        self.assertEqual(str(like), 'Django Testing')