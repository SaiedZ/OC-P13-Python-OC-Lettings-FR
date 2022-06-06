"""
Admin site for profiles app.
"""

from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
