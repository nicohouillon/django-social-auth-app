from django import forms
from django_select2.forms import Select2MultipleWidget
from lab_hacker.repository.models import Repository, Tag


class RepositoryForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=Select2MultipleWidget)

    class Meta:
        model = Repository
        fields = ('tags',)
        widgets = {'tags': Select2MultipleWidget()}
