# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-01-30 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20160131_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='condition',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
