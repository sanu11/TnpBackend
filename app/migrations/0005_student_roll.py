# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170103_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]