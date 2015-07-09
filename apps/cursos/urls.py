# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.cursos, name='cursos'),
    url(r'^(?P<curso_id>\d+)/$', views.curso_detalhes, name='curso_detalhes'),
    url(r'^disciplinas/$', views.disciplinas, name='disciplinas'),
    url(r'^disciplinas/(?P<disciplina_id>\d+)/$', views.disciplina_detalhes,
        name='disciplina_detalhes'),
]
