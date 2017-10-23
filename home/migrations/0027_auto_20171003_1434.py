# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-03 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_contenido_destacar'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tematica',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contenido',
            name='anoPublicacion',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='anoPublicacion',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
