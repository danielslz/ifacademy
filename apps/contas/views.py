# coding=utf-8

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from apps.contas.models import Perfil
from .forms import AutenticarForm, ConfiguracoesForm, PerfilForm


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
                return redirect(request.GET.get('next') or 'inicio')
            else:
                contexto['erro'] = u'Usuário e/ou senha inválido(s).'
    else:
        formulario = AutenticarForm()
    contexto['formulario'] = formulario
    return render(request, 'contas/entrar.html', contexto)


@login_required
def sair(request):
    logout(request)
    return redirect('inicio')


@login_required
def configuracoes(request):
    contexto = {}
    try:
        perfil = request.user.perfil
    except Perfil.DoesNotExist:
        perfil = None
    if request.method == 'POST':
        formulario = ConfiguracoesForm(request.POST, instance=request.user)
        formulario_perfil = PerfilForm(request.POST, files=request.FILES, instance=perfil)
        if formulario.is_valid() and formulario_perfil.is_valid():
            formulario.save()
            if perfil is None:
                perfil = formulario_perfil.save(commit=False)
                perfil.usuario = request.user
                perfil.save()
            else:
                formulario_perfil.save()
            contexto['sucesso'] = u'Suas configurações foram salvas com sucesso!'
    else:
        formulario = ConfiguracoesForm(instance=request.user)
        formulario_perfil = PerfilForm(instance=perfil)
    contexto['formulario'] = formulario
    contexto['formulario_perfil'] = formulario_perfil
    return render(request, 'contas/configuracoes.html', contexto)


@login_required
def perfil(request):
    contexto = {}
    return render(request, 'contas/perfil.html', contexto)
