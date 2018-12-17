#coding: utf-8
__author__ = "Lário dos Santos Diniz"


from django.db import models
from django.utils.translation import ugettext_lazy as translater


class Project(models.Model):
    """Entidade referente aos projetos open source"""
    name = models.CharField(translater('Name'), max_length=100)
    url_git = models.CharField(translater('Url Git'), max_length=100, blank=True)

    description = models.TextField(translater('Description'), blank=True)

    class Meta:
        verbose_name = translater('Project')
        verbose_name_plural = translater('Projects')
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass