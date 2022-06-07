"""
Tests for the teams views.
"""

from django.test import TestCase
from django.test import Client
from django.urls import reverse

PROFILE_INDEX_URL = reverse("profiles_index")


class ProfilesTests(TestCase):
    """Test profiles views."""

    def setUp(self):
        self.client = Client()

    def test_http_response_code_index(self):
        """Test http response for the index page."""
        res = self.client.get(PROFILE_INDEX_URL)
        self.assertEqual(res.status_code, 200)

    def test_http_response_content_index(self):
        """Test http content for the index page."""
        res = self.client.get(PROFILE_INDEX_URL)
        self.assertInHTML("Profiles", res.content.decode())
        self.assertContains(res, "Profiles")
