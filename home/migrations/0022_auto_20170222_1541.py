# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-22 21:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_tematica_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tematica',
            old_name='slug',
            new_name='slugTematica',
        ),
    ]
