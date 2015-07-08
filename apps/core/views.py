# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Oi Mundo")
    context = {
        'title': u'Gerenciador Acadêmico',
        'exists': None,
    }
    return render(request, 'index.html', context)
