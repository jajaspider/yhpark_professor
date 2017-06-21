# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-20 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yhpark', '0003_notice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='file',
            new_name='notice_file',
        ),
        migrations.AddField(
            model_name='notice',
            name='post_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notice',
            name='notice_url',
            field=models.URLField(default='http://sonagod.tk:20017'),
        ),
    ]
