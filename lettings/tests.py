"""
Tests for the teams views.
"""

from django.test import TestCase
from django.test import Client
from django.urls import reverse

from lettings import views  # noqa
from lettings import models  # noqa

LETTING_INDEX_URL = reverse("lettings:lettings_index")


class LettingsTests(TestCase):
    """Test lettings views."""

    def setUp(self):
        self.client = Client()

    def test_http_response_code_index(self):
        """Test http response for the index page."""
        res = self.client.get(LETTING_INDEX_URL)
        self.assertEqual(res.status_code, 200)

    def test_http_response_content_index(self):
        """Test http content for the index page."""
        res = self.client.get(LETTING_INDEX_URL)
        self.assertInHTML("Lettings", res.content.decode())
        self.assertContains(res, "Lettings")

    '''def test_http_response_code_letting_page(self):
        """Test http response for the letting page."""
        letting_obj = models.Letting.objects.create(
            title="Letting object for test",
            address=models.Address.objects.create(
                number=9999,
                street="",
                city="",
                state="78",
                zip_code="78000",
            ),
        )
        LETTING_URL = reverse("lettings:letting", kwargs={'letting_id': letting_obj.id})
        res = self.client.get(LETTING_URL)

        self.assertEqual(res.status_code, 200)
        self.assertInHTML(letting_obj.title, res.content.decode())'''
