import pytest
from django.urls import reverse
from django.test import Client
from elenizado.models import Publication, Evenement
from about.models import Gallerie
from website.models import SiteInfo
from django.core.paginator import Paginator


@pytest.mark.django_db
def test_index_view():
    # Set up data
    site_info = SiteInfo.objects.create(status=True, some_field="Test info")
    publication = Publication.objects.create(title="Test publication", content="Test content", date_add="2024-11-25")
    event = Evenement.objects.create(name="Test Event", description="Test event description", date_add="2024-11-25")
    gallery_item = Gallerie.objects.create(image="test_image.jpg", status=True)

    # Create a client to simulate a request
    client = Client()

    # Request the index page
    response = client.get(reverse('index'))

    # Check if the response is successful
    assert response.status_code == 200

    # Check if the data is passed in the context
    assert 'publication_r' in response.context
    assert 'events_r' in response.context
    assert 'gallerie' in response.context
    assert 'site_info' in response.context

    # Check if paginated content is present
    assert len(response.context['pub']) == 1  # Only one publication is created, so pagination should work.
    
    # Check if the content is rendered properly
    assert "Test publication" in response.content.decode()
    assert "Test Event" in response.content.decode()
    assert "Test info" in response.content.decode()

