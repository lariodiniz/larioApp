#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.contrib import admin

from .models import Project

class ProjectAdmin(admin.ModelAdmin):

    list_display = ['name', 'description', 'url_git']
    search_fields = ['name']

admin.site.register(Project, ProjectAdmin)