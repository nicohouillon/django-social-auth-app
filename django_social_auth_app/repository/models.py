from django.db import models
from django_social_auth_app.user.models import User


class Tag(models.Model):
    title = models.CharField(
        'Tag Tittle',
        max_length=35,
        help_text='Ex: Devops, python',
        unique=True
    )

    def __str__(self):
        return self.title

class Repository(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return '%d, %s, (%s), (%s)' % (
                self.id,
                self.name,
                self.description,
                'teste'
                ', '.join(tag.title for tag in self.tags.all())
            )
