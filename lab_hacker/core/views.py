from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from social_django.models import UserSocialAuth
import requests
import json


def get_repositories_list(github_login):
    access_token = github_login['access_token']
    github_user = github_login['login']

    user_header = {
                   'Authorization': access_token,
                   'Content-Type': 'application/json'
                  }

    response = requests.get('https://api.github.com/users/{}/repos'.format(github_user))
    repositories_list = response.json()

    return repositories_list

@login_required
def home(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    repositories_list = get_repositories_list(github_login.extra_data)

    return render(request, 'core/home.html', {'github_login': github_login,
                                              'repositories_list': repositories_list})
