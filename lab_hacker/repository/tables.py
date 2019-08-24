import django_tables2 as tables
from .models import Repository

class RepositoryTable(tables.Table):
    class Meta:
        model = Repository
        template_name = 'django_tables2/bootstrap.html'
