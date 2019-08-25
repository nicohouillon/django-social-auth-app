import django_tables2 as tables
from .models import Repository
from django_tables2 import TemplateColumn


class RepositoryTable(tables.Table):
    class Meta:
        model = Repository
        template_name = 'django_tables2/bootstrap.html'

        def render_tags(self, record):
            if record.tags.all():
                return mark_safe('<a href='+reverse("home", args=[record.pk])+'>'+
                            tags_list+'</a>')
            return '-'

        fields = ('id', 'name', 'description', 'tags', 'edit')

    edit = TemplateColumn(template_name='repository/tables/repository_update_column.html')
