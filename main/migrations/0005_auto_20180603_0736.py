# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-03 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180603_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='url_name',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
