# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-01 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mamtaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneytocollect',
            name='remark',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
