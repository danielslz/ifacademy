from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class SuporteViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('suporte')

    def test_acesso_suporte_sem_login(self):
        cliente = Client()
        resposta = cliente.get(self.url)
        self.assertEquals(resposta.status_code, 200)

    def test_suporte_template_usado(self):
        cliente = Client()
        respota = cliente.get(self.url)
        self.assertTemplateUsed(respota, 'suporte.html')
