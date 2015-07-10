# coding=utf-8
from django import forms
from .models import Suporte


# class SuporteForm(forms.Form):
#     assunto = forms.CharField(label='Assunto')
#     mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)
#     data = forms.DateField(label='Data do Ocorrido', required=False)
#
#     def __init__(self, *args, **kwargs):
#         super(SuporteForm, self).__init__(*args, **kwargs)
#         self.fields['assunto'].widget.attrs['class'] = 'form-control'
#         self.fields['mensagem'].widget.attrs['class'] = 'form-control'
#         for nome, campo in self.fields.items():
#             campo.widget.attrs['class'] = 'form-control'

class SuporteForm(forms.ModelForm):
    class Meta:
        model = Suporte
        fields = ['assunto', 'mensagem']
