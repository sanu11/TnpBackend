# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20170104_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default='Female', max_length=10),
            preserve_default=False,
        ),
    ]