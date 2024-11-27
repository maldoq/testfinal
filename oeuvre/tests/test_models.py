import pytest
from django.utils.timezone import now
from oeuvre.models import Poesie


@pytest.mark.django_db
class TestPoesieModel:

    def test_create_poesie(self):
        """
        Test creating a Poesie object and verify its fields.
        """
        poesie = Poesie.objects.create(
            titre="Beautiful Poem",
            description="This is a description of a beautiful poem.",
            poeme="<p>This is the poem content in HTML format.</p>",
            status=True,
        )

        assert poesie.titre == "Beautiful Poem"
        assert poesie.description == "This is a description of a beautiful poem."
        assert poesie.poeme == "<p>This is the poem content in HTML format.</p>"
        assert poesie.status is True
        assert poesie.date_add is not None
        assert poesie.date_update is not None

    def test_poesie_str_method(self):
        """
        Test the string representation of the Poesie object.
        """
        poesie = Poesie.objects.create(
            titre="My Poem",
            description="Another poem.",
            poeme="<p>Poem content.</p>",
            status=True,
        )

        assert str(poesie) == "My Poem"

    def test_poesie_default_status(self):
        """
        Test that the default value for status is True.
        """
        poesie = Poesie.objects.create(
            titre="Default Status Poem",
            description="Checking default status.",
            poeme="<p>Default content.</p>",
        )

        assert poesie.status is True

    def test_poesie_date_fields(self):
        """
        Test that `date_add` and `date_update` fields are correctly set.
        """
        before_creation = now()
        poesie = Poesie.objects.create(
            titre="Date Test Poem",
            description="Checking date fields.",
            poeme="<p>Checking date content.</p>",
            status=True,
        )
        after_creation = now()

        assert before_creation <= poesie.date_add <= after_creation
        assert before_creation <= poesie.date_update <= after_creation
