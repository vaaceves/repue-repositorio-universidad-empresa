# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-06 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20170206_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='evento',
            name='evento',
            field=models.CharField(max_length=150),
        ),
    ]
