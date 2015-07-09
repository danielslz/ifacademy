# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='T\xedtulo', db_column=b'titulo_txt')),
                ('descricao', models.TextField(verbose_name='Descri\xe7\xe3o', blank=True)),
                ('inicio_em', models.DateField(null=True, verbose_name='In\xedcio em', blank=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'ordering': ['titulo'],
                'db_table': 'cursos',
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('descricao', models.TextField(verbose_name='Descri\xe7\xe3o', blank=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('curso', models.ForeignKey(verbose_name='Curso', to='cursos.Curso')),
            ],
            options={
                'ordering': ['titulo'],
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
            },
        ),
    ]
