# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0005_auto_20150709_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='inscritos',
            field=models.ManyToManyField(related_name='cursos', verbose_name='Inscritos', to=settings.AUTH_USER_MODEL),
        ),
    ]
