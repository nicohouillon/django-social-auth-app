from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    playedHours = models.FloatField(default = 0)
    email = models.EmailField(max_length=254)

    #objects = CustomUserManager()

    #playedSongs = models.ManyToManyField(Song, blank=True, null = True)
    #invitedFriends = models.ManyToManyField('self', blank = True, null = True)
