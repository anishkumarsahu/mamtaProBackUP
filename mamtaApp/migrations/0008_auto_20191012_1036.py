# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-12 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import mamtaApp.models


class Migration(migrations.Migration):
    dependencies = [
        ('mamtaApp', '0007_auto_20190902_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='staffuser',
            name='companyID',
            field=models.FloatField(blank=True, null=True, verbose_name=mamtaApp.models.Company),
        ),
    ]
