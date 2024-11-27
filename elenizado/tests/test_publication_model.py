from django.test import TestCase
from django.urls import reverse
from elenizado.models import Categorie, Publication, Commentaire, ReponseCommentaire, Like, Evenement, Cours, Textes, Video
from django.utils.text import slugify
from datetime import datetime

class PublicationModelTest(TestCase):

    def test_publication_creation(self):
        categorie = Categorie.objects.create(
            nom='Technology',
            description='Category for tech publications'
        )
        publication = Publication.objects.create(
            titre='Django Testing',
            description='This is a test post for Django testing',
            categorie=categorie
        )
        self.assertEqual(publication.titre, 'Django Testing')
        self.assertEqual(publication.categorie.nom, 'Technology')
        self.assertTrue(publication.status)
        self.assertIsNotNone(publication.slug)

    def test_slug_creation_on_save(self):
        categorie = Categorie.objects.create(
            nom='Technologys',
            description='Category for tech publications'
        )
        publicationx = Publication.objects.create(
            titre='Djangos Testing',
            description='This is a test post for Django testing',
            categorie=categorie
        )
        slug = '-'.join((slugify(publicationx.titre), slugify(datetime.now().microsecond)))
        self.assertTrue(publicationx.slug.startswith(slug))

    def test_publication_str(self):
        categorie = Categorie.objects.create(
            nom='Technology',
            description='Category for tech publications'
        )
        publication = Publication.objects.create(categorie=categorie,titre='Testssss Post', description='A description of the post')
        self.assertEqual(str(publication), 'Testssss Post')