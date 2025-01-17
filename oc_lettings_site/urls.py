"""
app's urls module.
"""

from django.contrib import admin
from django.urls import path, include

from . import views


def trigger_error(request):
    """Generate error in order
    to test sentry.
    """
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('', views.index, name='index'),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
