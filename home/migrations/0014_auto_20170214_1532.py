# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-14 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_contenido_nombrecortourl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='nombreCortoURL',
            field=models.CharField(default='texto separado por guiones bajos', max_length=80),
        ),
    ]
