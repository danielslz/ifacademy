# coding=utf-8

from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(
        r'^$', views.cursos, name='cursos'
    ),
    url(
        r'^(?P<pk>\d+)/$', views.curso_detalhes, 
        name='curso_detalhes'
    ),
]
