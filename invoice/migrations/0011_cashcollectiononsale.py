# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-02-17 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('mamtaApp', '0012_moneycollection_companyid'),
        ('invoice', '0010_auto_20200201_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashCollectionOnSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('customerName', models.CharField(blank=True, max_length=200, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('lastUpdatedOn', models.DateTimeField(auto_now=True)),
                ('companyID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                to='mamtaApp.Company')),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                to='mamtaApp.StaffUser')),
            ],
        ),
    ]
