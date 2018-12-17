#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.contrib import admin
from django.urls import path, include

from core.views import index


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]
