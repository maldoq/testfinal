from django.test import TestCase
from django.urls import reverse
from elenizado.models import Categorie, Publication, Commentaire, ReponseCommentaire, Like, Evenement, Cours, Textes, Video
from django.utils.text import slugify
from datetime import datetime

class VideoModelTest(TestCase):

    def test_video_creation(self):
        video = Video.objects.create(
            titre='Django Tutorial',
            description='An in-depth tutorial on Django',
            video='https://www.youtube.com/watch?v=xyz123'
        )
        self.assertEqual(video.titre, 'Django Tutorial')

    def test_video_str(self):
        video = Video.objects.create(
            titre='Django Tutorial',
            description='An in-depth tutorial on Django',
            video='https://www.youtube.com/watch?v=xyz123'
        )
        self.assertEqual(str(video), 'Django Tutorial')
