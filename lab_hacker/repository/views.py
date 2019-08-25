from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from lab_hacker.repository.models import Repository, Tag
from lab_hacker.repository.forms.forms import RepositoryForm
import requests
import json
from lab_hacker.repository.models import Tag
from lab_hacker.repository.tables import TagTable
from django_tables2 import RequestConfig


def instantiate_repository(repository, user):
    name = repository['name']
    description = repository['description'] or ""

    obj, created = Repository.objects.update_or_create(
        name=name, owner=user,
        defaults={'description': description}
    )

def create_repositories(repositories_list, user):
    for repository in repositories_list:
        instantiate_repository(repository, user)

@login_required
def edit_repository_tags(request, repository_id):
    user = request.user
    repository = Repository.objects.get(id=repository_id) 

    form = RepositoryForm()

    tags_table = TagTable(Tag.objects.all())
    RequestConfig(request).configure(tags_table)

    return render(request, 'repository/edit/edit_tags.html', {'repository': repository,
                                                              'form': form,
                                                              'tags_table': tags_table})

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

@login_required
def new_tag(request, repository_id):
    title = request.POST.get("tag_title", "")

    tag, created = Tag.objects.get_or_create(
        title=title
    )

    repository = Repository.objects.get(id=repository_id)
    repository.tags.add(tag)
    repository.save()

    response = redirect('/edit_repository_tags/{}'.format(repository_id))
    return response
