# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0010_auto_20171013_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data_log',
            name='sn_ticket',
        ),
        migrations.AlterField(
            model_name='data_log',
            name='request_ticket',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='data_log',
            name='transfer_ticket',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]