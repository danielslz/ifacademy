# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='T\xedtulo'),
        ),
        migrations.AlterModelTable(
            name='curso',
            table=None,
        ),
    ]
