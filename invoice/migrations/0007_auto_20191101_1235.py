# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-11-01 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('invoice', '0006_collectiononsale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceseries',
            name='series',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
