# coding=utf-8

from django.contrib import admin

from .models import Curso, Disciplina

# admin.site.register([Curso, Disciplina])
class CursoAdmin(admin.ModelAdmin):

    list_display = [
        'titulo', 'criado_em', 'modificado_em'
    ]
    search_fields = ['titulo', 'descricao']
    list_filter = ['criado_em', 'modificado_em']


class DisciplinaAdmin(admin.ModelAdmin):

    list_display = [
        'titulo', 'curso', 'criado_em', 'modificado_em'
    ]
    search_fields = ['titulo', 'descricao']
    list_filter = ['criado_em', 'modificado_em']


admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
