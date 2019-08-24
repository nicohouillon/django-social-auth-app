import django_tables2 as tables
from .models import Repository

class RepositoryTable(tables.Table):
    class Meta:
        model = Repository
        template_name = 'django_tables2/bootstrap.html'

        fields = ('id', 'name', 'description', 'tags')

        tags = tables.Column(empty_values=(), orderable=False)

        def render_tags(self, record):
            if record.tags.all():
                return ', '.join([tag.name for tag in record.tags.all()])
            return '-'
