# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-18 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20170618_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='diploma_board',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_board',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_schoolname',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='tenth_yeargap_reason',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelveth_board',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelveth_schoolname',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelveth_yeargap_reason',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
