# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='descript',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]
