# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-15 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20170215_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='descarga',
            field=models.URLField(default='http://www.redue-alcue.org'),
        ),
    ]
