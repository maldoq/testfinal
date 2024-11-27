import pytest
from django.urls import reverse
from django.test import Client
from website.models import Newsletter

@pytest.mark.django_db
def test_is_newsletter_view():
    # Create a client to simulate a request
    client = Client()

    # Define a valid email
    valid_email = "test@example.com"
    
    # Send a POST request with valid email
    response = client.post(reverse('is_newsletter'), {'email': valid_email})

    # Check if the response status code is 200
    assert response.status_code == 200
    
    # Parse the response JSON
    response_data = response.json()

    # Check if the response indicates success
    assert response_data['success'] is True
    assert response_data['message'] == "l'enregistrement a bien été effectué"
    
    # Check if the email was saved in the database
    assert Newsletter.objects.filter(email=valid_email).exists()


@pytest.mark.django_db
def test_is_newsletter_invalid_email():
    # Create a client to simulate a request
    client = Client()

    # Define an invalid email
    invalid_email = "invalid-email"

    # Send a POST request with invalid email
    response = client.post(reverse('is_newsletter'), {'email': invalid_email})

    # Check if the response status code is 200
    assert response.status_code == 200
    
    # Parse the response JSON
    response_data = response.json()

    # Check if the response indicates failure
    assert response_data['success'] is False
    assert response_data['message'] == "email incorrect"

    # Check that the invalid email was not saved in the database
    assert not Newsletter.objects.filter(email=invalid_email).exists()
