# coding=utf-8

from django.db import models


class Curso(models.Model):

    titulo = models.CharField(
        u'Título', max_length=100,
    )
    descricao = models.TextField(
        u'Descrição', blank=True
    )
    inicio_em = models.DateField(
        u'Início em', null=True, blank=True
    )
    criado_em = models.DateTimeField(
        u'Criado em', auto_now_add=True
    )
    modificado_em = models.DateTimeField(
        u'Modificado em', auto_now=True
    )

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = u'Curso'
        verbose_name_plural = u'Cursos'
        ordering = ['titulo']


class Disciplina(models.Model):

    curso = models.ForeignKey(
        Curso, verbose_name=u'Curso', related_name='disciplinas'
    )
    titulo = models.CharField(
        u'Título', max_length=100
    )
    descricao = models.TextField(
        u'Descrição', blank=True
    )
    criado_em = models.DateTimeField(
        u'Criado em', auto_now_add=True
    )
    modificado_em = models.DateTimeField(
        u'Modificado em', auto_now=True
    )

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = u'Disciplina'
        verbose_name_plural = u'Disciplinas'
        ordering = ['titulo']
