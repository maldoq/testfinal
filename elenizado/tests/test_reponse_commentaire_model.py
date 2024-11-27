from django.test import TestCase
from django.urls import reverse
from elenizado.models import Categorie, Publication, Commentaire, ReponseCommentaire, Like, Evenement, Cours, Textes, Video
from django.utils.text import slugify
from datetime import datetime

class ReponseCommentaireModelTest(TestCase):

    def test_reponse_creation(self):
        categorie = Categorie.objects.create(
            nom='Technology',
            description='Category for tech publications'
        )
        publication = Publication.objects.create(
            titre='Django Testing',
            description='This is a test post for Django testing',
            categorie=categorie
        )
        commentaire = Commentaire.objects.create(
            publication=publication,
            nom='John Doe',
            commentaire='Great article!'
        )
        reponse = ReponseCommentaire.objects.create(
            commentaire=commentaire,
            nom='Admin',
            reponse='Thank you!'
        )
        self.assertEqual(reponse.nom, 'Admin')
        self.assertEqual(reponse.reponse, 'Thank you!')