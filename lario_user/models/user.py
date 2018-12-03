#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import re

from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext as translater


class User(AbstractBaseUser, PermissionsMixin):
    """
    Entity model System user
    """

    username = models.CharField(
        translater('Nickname / User'), max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                translater('Please enter a valid username.'),
                translater('This value should contain only letters, numbers and the characters: @ /. / + / - / _.'),
                'invalid'
            )
        ], help_text=translater('A short name that will be used to uniquely identify it on the platform.'),
    )
    name = models.CharField(translater('Name'), max_length=100, blank=True)
    email = models.EmailField(translater('E-mail'), unique=True)
    is_staff = models.BooleanField(translater('Staff'), default=False)
    is_active = models.BooleanField(translater('Active'), default=True)
    date_joined = models.DateTimeField(translater('Entry date'), auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = translater('User')
        verbose_name_plural = translater('Users')

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]
