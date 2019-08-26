import django_tables2 as tables
from .models import Repository, Tag
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

        fields = ('id', 'name', 'description', 'tags', 'edit_tags', 'remove_repository')

    edit_tags = TemplateColumn(template_name='repository/tables/update_repository_tags.html')
    remove_repository = TemplateColumn(template_name='repository/tables/remove_repository.html')

class TagTable(tables.Table):
    class Meta:
        model = Tag
        template_name = 'django_tables2/bootstrap.html'

        fields = ('id', 'title',)
