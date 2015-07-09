# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_curso_inicio_em'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='curso',
            field=models.ForeignKey(related_name='disciplinas', verbose_name='Curso', to='cursos.Curso'),
        ),
    ]
