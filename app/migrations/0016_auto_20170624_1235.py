# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-24 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20170624_1159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='be_college_name',
            new_name='be_collegename',
        ),
    ]
