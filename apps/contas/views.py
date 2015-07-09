# coding=utf-8

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import AutenticarForm, ConfiguracoesForm


def entrar(request):
    if request.user.is_authenticated():
        return redirect('inicio')
    contexto = {}
    if request.method == 'POST':
        formulario = AutenticarForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['usuario']
            senha = formulario.cleaned_data['senha']
            usuario_valido = authenticate(username=usuario, password=senha)
            if usuario_valido:
                login(request, usuario_valido)
                return redirect('inicio')
            else:
                contexto['erro'] = u'Usuário e/ou senha inválido(s).'
    else:
        formulario = AutenticarForm()
    contexto['formulario'] = formulario
    return render(request, 'contas/entrar.html', contexto)


def sair(request):
    logout(request)
    return redirect('entrar')


def configuracoes(request):
    contexto = {}
    if request.method == 'POST':
        formulario = ConfiguracoesForm(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            contexto['sucesso'] = u'Dados alterados com sucesso!'
    else:
        formulario = ConfiguracoesForm(instance=request.user)
    contexto['formulario'] = formulario
    return render(request, 'contas/configuracoes.html', contexto)
