# coding=utf-8

from django import forms


class AutenticarForm(forms.Form):
    usuario = forms.CharField(label=u'Usuário')
    senha = forms.CharField(label=u'Senha', widget=forms.PasswordInput)
