# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 02:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0003_auto_20170913_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwarePurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_creation', models.DateField(auto_now_add=True)),
                ('record_update', models.DateField(auto_now=True)),
                ('date_purchased', models.DateField(auto_now=True)),
                ('units_purchased', models.IntegerField()),
                ('cost_per_unit', models.FloatField()),
                ('invoice_number', models.CharField(max_length=64)),
                ('sn_ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dc_management.SN_Ticket')),
            ],
        ),
        migrations.CreateModel(
            name='SoftwareUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_creation', models.DateField(auto_now_add=True)),
                ('record_update', models.DateField(auto_now=True)),
                ('unit', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='software',
            name='cost_per_unit',
        ),
        migrations.RemoveField(
            model_name='software',
            name='sn_ticket',
        ),
        migrations.RemoveField(
            model_name='software',
            name='unit',
        ),
        migrations.AddField(
            model_name='softwarepurchase',
            name='sw_purchased',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dc_management.Software'),
        ),
        migrations.AddField(
            model_name='softwarepurchase',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dc_management.SoftwareUnit'),
        ),
    ]