# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assunto', models.CharField(max_length=100, verbose_name='Assunto')),
                ('mensagem', models.TextField(verbose_name='Mensagem')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
            options={
                'ordering': ['-criado_em'],
                'verbose_name': 'Suporte',
                'verbose_name_plural': 'Suportes',
            },
        ),
    ]
