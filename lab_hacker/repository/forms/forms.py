from django import forms
from django_select2.forms import Select2MultipleWidget
from lab_hacker.repository.models import Repository, Tag

class RepositoryForm(forms.ModelForm):
    class Meta:
        model = Repository
        fields = ('tags',)
        widgets = {'tags': Select2MultipleWidget}

    def __init__(self, pre_setted_tags, *args, **kwargs):
        super(RepositoryForm, self).__init__(*args, **kwargs)
        self.fields['tags'].initial = pre_setted_tags
