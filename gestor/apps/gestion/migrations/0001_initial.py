# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2020-03-08 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuario_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_cuenta', models.CharField(max_length=50)),
                ('usuario_pass', models.CharField(max_length=20)),
            ],
        ),
    ]
