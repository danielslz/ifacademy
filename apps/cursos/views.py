# coding=utf-8

from django.shortcuts import render
from .models import Curso


def cursos(request):
    contexto = {}
    contexto['cursos'] = Curso.objects.all()
    return render(
        request, 'cursos/cursos.html', contexto
    )


def curso_detalhes(request, pk):
    curso = Curso.objects.get(pk=pk)
    contexto = {
        'curso': curso
    }
    return render(
        request, 'cursos/curso_detalhes.html', contexto
    )
