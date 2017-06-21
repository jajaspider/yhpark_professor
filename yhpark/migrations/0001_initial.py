# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 08:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('force', models.CharField(max_length=500)),
                ('research', models.CharField(max_length=500)),
                ('academy', models.CharField(max_length=500)),
                ('awards', models.CharField(max_length=500)),
                ('student', models.CharField(max_length=500)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]