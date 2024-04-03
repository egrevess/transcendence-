from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.conf import settings

def start_oauth(request):
    authorization_url = "https://api.intra.42.fr/oauth/authorize?client_id={}&redirect_uri={}&response_type=code&scope=public".format(
        settings.SOCIAL_AUTH_API42_KEY, settings.SOCIAL_AUTH_API42_REDIRECT_URI)
    return redirect(authorization_url)


def	pong_view(request):
	return render(request, 'game/pong.html')


