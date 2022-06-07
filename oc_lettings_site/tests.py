"""
Tests for the index view.
"""

from django.test import TestCase
from django.test import Client
from django.urls import reverse

INDEX_URL = reverse("index")


class IndexTests(TestCase):
    """Test index view."""

    def setUp(self):
        self.client = Client()

    def test_http_response_code_index(self):
        """Test http response for the index page."""
        res = self.client.get(INDEX_URL)
        self.assertEqual(res.status_code, 200)

    def test_http_response_content_index(self):
        """Test http content for the index page."""
        res = self.client.get(INDEX_URL)
        self.assertInHTML("<h1>Welcome to Holiday Homes</h1>", res.content.decode())
