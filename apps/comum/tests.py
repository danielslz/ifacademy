# coding=utf-8

from django.test import TestCase, Client
from django.core import mail
from django.core.urlresolvers import reverse


class SuporteViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('suporte')
        self.cliente = Client()

    def tearDown(self):
        del self.url
        del self.cliente

    def test_acesso_sem_login(self):
        resposta = self.cliente.get(self.url)
        self.assertEquals(resposta.status_code, 200)

    def test_template_usado(self):
        resposta = self.cliente.get(self.url)
        self.assertContains(resposta, 'Suporte')
        self.assertTemplateUsed(resposta, 'suporte.html')

    def test_formulario_ok(self):
        dados = {
            'assunto': 'Assunto de teste',
            'mensagem': 'Mensagem de teste'
        }
        resposta = self.cliente.post(self.url, dados)
        self.assertTrue('formulario' in resposta.context)

    def test_enviou_email(self):
        dados = {
            'assunto': 'Assunto de teste',
            'mensagem': 'Mensagem de teste'
        }
        self.cliente.post(self.url, dados)
        self.assertEquals(len(mail.outbox), 1)

    def test_erro_formulario_sem_assunto(self):
        dados = {
            'assunto': '',
            'mensagem': 'Mensagem de teste'
        }
        resposta = self.cliente.post(self.url, dados)
        self.assertFormError(resposta, 'formulario', 'assunto', u'Este campo é obrigatório.')

    def test_erro_formulario_sem_mensagem(self):
        dados = {
            'assunto': 'Assunto de teste',
            'mensagem': ''
        }
        resposta = self.cliente.post(self.url, dados)
        self.assertFormError(resposta, 'formulario', 'mensagem', u'Este campo é obrigatório.')