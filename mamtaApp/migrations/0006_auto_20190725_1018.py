# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-25 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mamtaApp', '0005_staffuser_cantakepayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffuser',
            name='canTakePayment',
            field=models.BooleanField(default=True),
        ),
    ]
