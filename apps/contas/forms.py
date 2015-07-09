# coding=utf-8

from django import forms
from django.contrib.auth.models import User


class AutenticarForm(forms.Form):
    usuario = forms.CharField(label=u'Usuário')
    senha = forms.CharField(label=u'Senha', widget=forms.PasswordInput)


class PerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
