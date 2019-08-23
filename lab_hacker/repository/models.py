from django.db import models
from lab_hacker.user.models import CustomUserSocialAuth


class Repository(models.Model):
    owner = models.ForeignKey(CustomUserSocialAuth, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
