# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-12-04 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeattendance',
            name='loginSystemID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='attendance.LoginSystem'),
        ),
    ]