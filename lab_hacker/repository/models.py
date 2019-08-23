from django.db import models
from lab_hacker.user.models import User


class Repository(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Tag(models.Model):

    title = models.CharField(
        _('Tag Tittle'),
        max_length=30,
        choices=AWARDS_CHOICES,
        default=AWARDS_CHOICES[0][0],
        help_text=_('Ex: Melhor Jogo.')
    )

    color = models.CharField(
        _('Colocação'),
        max_length=30,
        choices=PLACE_AWARDS_CHOICES,
        default=PLACE_AWARDS_CHOICES[0][0],
        help_text=_('Colocação que o jogo ganhou.')
    )

    def __str__(self):
        return self.name

