# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yhpark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='academy',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='professor',
            name='author',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='professor',
            name='awards',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='professor',
            name='force',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='professor',
            name='research',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='professor',
            name='student',
            field=models.TextField(),
        ),
    ]
