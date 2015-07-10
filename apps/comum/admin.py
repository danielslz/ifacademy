# coding=utf-8

from django.contrib import admin
from .models import Suporte


class SuporteAdmin(admin.ModelAdmin):
    list_display = ['assunto', 'criado_em']
    search_fields = ['assunto', 'mensagem']

admin.site.register(Suporte, SuporteAdmin)
