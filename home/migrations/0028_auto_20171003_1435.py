# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-03 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20171003_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='tematica',
            name='slug',
            field=models.SlugField(),
        ),
    ]
