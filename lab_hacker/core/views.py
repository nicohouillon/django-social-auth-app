from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from social_django.models import UserSocialAuth
import requests
import json
from lab_hacker.repository.models import Repository


#def instantiate_repository(repository, user_id):
#    Repository.create(owner=user_id, name=repository.name, description=repositories.description)
#
#def create_repositories(repositories_list, user_id):
#    for repository in repositories_list:
#        print("\n\n\n\n")
#        print(repository)
#        print("\n\n\n\n")
#
#        instantiate_repository(repository, user_id)

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
    #create_repositories(repositories_list, user.id)

    return render(request, 'core/home.html', {'github_login': github_login,
                                              'repositories_list': repositories_list})
