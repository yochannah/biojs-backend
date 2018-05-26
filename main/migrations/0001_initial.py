# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-25 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('stars', models.IntegerField(default=0)),
                ('downloads', models.BigIntegerField(default=0)),
                ('created_time', models.DateTimeField(editable=False)),
                ('modified_time', models.DateTimeField()),
                ('icon_url', models.URLField(blank=True, null=True)),
                ('icon', models.ImageField(null=True, upload_to='icons/')),
                ('github_url', models.URLField(null=True)),
                ('short_description', models.TextField(null=True)),
                ('url_name', models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='component',
            name='tags',
            field=models.ManyToManyField(to='main.Tag'),
        ),
    ]