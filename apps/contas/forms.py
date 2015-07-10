# coding=utf-8

from django import forms
from django.contrib.auth.models import User
from .models import Perfil


class AutenticarForm(forms.Form):
    usuario = forms.CharField(label=u'Usuário')
    senha = forms.CharField(label=u'Senha', widget=forms.PasswordInput)


class ConfiguracoesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConfiguracoesForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['email'].error_messages['required'] = u'Preencha o e-mail'
        self.fields['email'].label = u'E-mail'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto', 'endereco']
