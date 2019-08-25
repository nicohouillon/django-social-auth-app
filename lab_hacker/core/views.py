from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from social_django.models import UserSocialAuth
from lab_hacker.repository.models import Repository
from lab_hacker.repository.tables import RepositoryTable
from django_tables2 import RequestConfig


@login_required
def home(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    tags_query_parameter = request.GET.get('tags')

    query_result = Repository.objects.all()

    repositories_table = RepositoryTable(Repository.objects.all())
    RequestConfig(request).configure(repositories_table)

    return render(request, 'core/home.html', {'github_login': github_login,
                                              'repositories_table': repositories_table})
