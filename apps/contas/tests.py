# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class PerfilViewTestCase(TestCase):
    def setUp(self):
        self.usuario = User()
        self.usuario.username = 'teste'
        self.usuario.set_password('teste')
        self.usuario.save()

    def tearDown(self):
        self.usuario.delete()

    def test_perfil_login_required(self):
        cliente = Client()
        resposta = cliente.get(reverse('perfil'))
        self.assertEquals(resposta.status_code, 302)
        cliente.login(username='teste', password='teste')
        resposta = cliente.get(reverse('perfil'))
        self.assertEquals(resposta.status_code, 200)

    def test_perfil_template_usado(self):
        cliente = Client()
        cliente.login(username='teste', password='teste')
        resposta = cliente.get(reverse('perfil'))
        self.assertTemplateUsed(resposta, 'contas/perfil.html')
