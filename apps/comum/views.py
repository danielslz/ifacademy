# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    contexto = {}
    return render(request, 'inicio.html', contexto)
