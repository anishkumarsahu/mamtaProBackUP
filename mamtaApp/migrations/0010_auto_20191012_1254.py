# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-12 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('mamtaApp', '0009_auto_20191012_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffuser',
            name='companyID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='mamtaApp.Company'),
        ),
    ]
