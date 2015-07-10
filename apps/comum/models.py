# coding=utf-8

from django.db import models
from django.conf import settings
from django.core.mail import send_mail


class Suporte(models.Model):
    assunto = models.CharField(u'Assunto', max_length=100)
    mensagem = models.TextField(u'Mensagem')
    criado_em = models.DateTimeField(u'Criado em', auto_now_add=True)

    def enviar_email(self):
        corpo_email = "Data: {0}\n{1}".format(self.criado_em, self.mensagem)
        send_mail(
            self.assunto,
            corpo_email,
            settings.DEFAULT_EMAIL_FROM,
            ['suporte@ifacademy.com']
        )

    def __unicode__(self):
        return self.assunto

    class Meta:
        verbose_name = 'Suporte'
        verbose_name_plural = 'Suportes'
        ordering = ['-criado_em']


def post_save_suporte(instance, **kwargs):
    instance.enviar_email()

models.signals.post_save.connect(post_save_suporte, sender=Suporte)
