# coding=utf-8

from django.contrib import admin
from .models import Perfil


class PerfilAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'foto']
    search_fields = ['usuario__username', 'usuario__email']

admin.site.register(Perfil, PerfilAdmin)
