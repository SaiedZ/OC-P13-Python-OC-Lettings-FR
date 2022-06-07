"""
Tests for the teams views.
"""

from django.test import TestCase
from django.test import Client
from django.urls import reverse

from django.contrib.auth import get_user_model
from profiles import models

USER_MODEL = get_user_model()
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

    def test_profile_page(self):
        """Test http response and data in the profile page."""
        profile = models.Profile.objects.create(
            favorite_city="City",
            user=USER_MODEL.objects.create(
                username='testuser',
            ),
        )
        PROFILE_URL = reverse("profile", kwargs={'username': profile.user.username})
        res = self.client.get(PROFILE_URL)

        self.assertEqual(res.status_code, 200)
        print(res.content.decode('utf-8'))
        self.assertInHTML(f'<p>Favorite city: {profile.favorite_city}</p>', res.content.decode())
