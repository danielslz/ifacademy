# coding=utf-8

from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.OneToOneField(User, verbose_name=u'Usuário', related_name='perfil')
    foto = models.ImageField('Foto', upload_to='fotos')
    endereco = models.TextField(u'Endereço', blank=True)

    def __unicode__(self):
        return unicode(self.usuario)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
