# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-31 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170131_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tematica',
            name='nombreTematica',
            field=models.CharField(max_length=100),
        ),
    ]
