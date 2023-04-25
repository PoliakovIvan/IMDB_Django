from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            is_superuser=True
            **kwargs
        )
        return user

class User(AbstractUser):
    USERNAME_FIELDS = 'email'
    REQUIRED_FIELDS=[]

    objects = UserManager

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