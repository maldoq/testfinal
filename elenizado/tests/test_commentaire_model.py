from django.test import TestCase
from django.urls import reverse
from elenizado.models import Publication, Commentaire, Categorie

class CommentaireModelTest(TestCase):

    def test_commentaire_creation(self):
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
        self.assertEqual(commentaire.nom, 'John Doe')
        self.assertEqual(commentaire.commentaire, 'Great article!')