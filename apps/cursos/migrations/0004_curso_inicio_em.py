# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_remove_curso_inicio_em'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='inicio_em',
            field=models.DateField(null=True, verbose_name='In\xedcio em', blank=True),
        ),
    ]
