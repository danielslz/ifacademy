# coding=utf-8

from django.contrib.auth.views import redirect_to_login
from django.conf import settings
from django.core.urlresolvers import reverse


class AutenticacaoObrigatoriaMiddleware(object):
    def process_request(self, request):
        url_de_login = reverse(settings.LOGIN_URL)
        if url_de_login != request.path and not request.user.is_authenticated():
            return redirect_to_login(request.path)
