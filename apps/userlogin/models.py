from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    USERNAME_FIELDS = 'email'
    REQUIRED_FIELDS=[]

    username = None
    email = models.EmailField(_('email adrdress'), null=False, unique=True)