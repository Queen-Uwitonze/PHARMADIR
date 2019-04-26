# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-26 16:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pharmapp', '0004_auto_20190426_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pharmacy',
            name='id',
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='user',
            field=models.OneToOneField(default=8, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
