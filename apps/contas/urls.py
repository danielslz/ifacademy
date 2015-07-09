# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^entrar$', views.entrar, name='entrar'),
    url(r'^sair$', views.sair, name='sair'),
    url(r'^perfil$', views.perfil, name='perfil'),
]
