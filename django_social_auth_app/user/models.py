from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class CustomUserManager(models.Manager):
    def create_user(self, username, email):
        return self.model._default_manager.create(username=username)

class User(AbstractBaseUser):
    username = models.CharField(max_length=100)
    last_login = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(max_length=254)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def __unicode__(self):
        return self.username

    def is_authenticated(self):
        return True    
