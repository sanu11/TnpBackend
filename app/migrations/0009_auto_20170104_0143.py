# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 20:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170104_0142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='col_id',
            new_name='college_id',
        ),
    ]
