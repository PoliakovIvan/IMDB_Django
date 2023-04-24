from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    USERNAME_FIELDS = 'email'
    REQUIRED_FIELDS=[]

    username = None
    email = models.EmailField(_('email adrdress'), null=False, unique=True)
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='userlogin_users')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='userlogin_users',
        help_text='Specific permissions for this user.',
    )