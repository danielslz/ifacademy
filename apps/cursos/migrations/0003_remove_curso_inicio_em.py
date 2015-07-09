# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20150708_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='inicio_em',
        ),
    ]
