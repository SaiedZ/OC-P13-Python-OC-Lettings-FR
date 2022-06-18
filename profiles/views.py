"""
Views for the profiles app.
"""

from django.shortcuts import render
from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d


def index(request):
    """The index function of the Profile model view.

    This view will show all the profiles in the database.

    Parameters
    ----------
    request : http request object.
        The request sent by the client.

    Returns
    -------
    A render of index.html page.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus
# et males


def profile(request, username):
    """The profile view of the Profile model.

    This view will show the detail of a profile using
    the id in the request parameters.

    Parameters
    ----------
    request : http request object.
        The request sent by the client.

    Returns
    -------
    A render of profile.html page.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
