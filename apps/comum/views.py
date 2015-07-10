# coding=utf-8

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import SuporteForm


def inicio(request):
    contexto = {}
    return render(request, 'inicio.html', contexto)


# def suporte(request):
#     contexto = {}
#     if request.method == 'POST':
#         formulario = SuporteForm(request.POST)
#         if formulario.is_valid():
#             assunto = formulario.cleaned_data['assunto']
#             mensagem = formulario.cleaned_data['mensagem']
#             send_mail(
#                 assunto,
#                 mensagem,
#                 "contato@email.com",
#                 ['danielslz@gmail.com']
#             )
#     else:
#         formulario = SuporteForm()
#     contexto['formulario'] = formulario
#     return render(request, 'suporte.html', contexto)

def suporte(request):
    contexto = {}
    formulario = SuporteForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        contexto['sucesso'] = u'Recebemos sua solicitação de suporte.'
    contexto['formulario'] = formulario
    return render(request, 'suporte.html', contexto)
