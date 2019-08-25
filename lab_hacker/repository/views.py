from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from lab_hacker.repository.models import Repository, Tag
import requests
import json


def instantiate_repository(repository, user):
    name = repository['name']
    description = repository['description'] or ""

    tag_1 = Tag(title='devops')
    tag_1.save()
    tag_2 = Tag(title='web')
    tag_2.save()
    tag_3 = Tag(title='database')
    tag_3.save()

    obj, created = Repository.objects.update_or_create(
        name=name, owner=user,
        defaults={'description': description}
    )

    obj.tags.add(tag_1)
    obj.tags.add(tag_2)
    obj.tags.add(tag_3)
    obj.save()

def create_repositories(repositories_list, user):
    for repository in repositories_list:
        instantiate_repository(repository, user)

@login_required
def edit_repository_tags(request, repository_id):
    user = request.user
    repository = Repository.objects.get(id=repository_id) 

    return render(request, 'repository/edit/edit.html', {'repository': repository})

@login_required
def get_repositories(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None


    access_token = github_login.extra_data['access_token']
    github_user = github_login.extra_data['login']

    user_header = {
                   'Authorization': access_token,
                   'Content-Type': 'application/json'
                  }

    response = requests.get('https://api.github.com/users/{}/repos'.format(github_user))
    repositories_list = response.json()

    create_repositories(repositories_list, user)

    response = redirect('/')
    return response
