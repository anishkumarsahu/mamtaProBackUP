# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-02-17 14:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('invoice', '0011_cashcollectiononsale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashcollectiononsale',
            name='companyID',
        ),
        migrations.RemoveField(
            model_name='cashcollectiononsale',
            name='createdBy',
        ),
        migrations.DeleteModel(
            name='CashCollectionOnSale',
        ),
    ]
