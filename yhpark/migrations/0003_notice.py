# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yhpark', '0002_auto_20170528_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('contents', models.TextField()),
                ('notice_url', models.URLField()),
                ('file', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
