# coding=utf-8

from django.shortcuts import render
from .models import Curso, Disciplina


def cursos(request):
    contexto = {}
    contexto['cursos'] = Curso.objects.all()
    return render(request, 'cursos/cursos.html', contexto)


def curso_detalhes(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    contexto = {
        'curso': curso
    }
    return render(request, 'cursos/curso_detalhes.html', contexto)


def disciplinas(request):
    contexto = {}
    contexto['disciplinas'] = Disciplina.objects.all()
    return render(request, 'cursos/disciplinas.html', contexto)


def disciplina_detalhes(request, disciplina_id):
    contexto = {}
    contexto['disciplina'] = Disciplina.objects.get(pk=disciplina_id)
    return render(request, 'cursos/disciplina_detalhes.html', contexto)
