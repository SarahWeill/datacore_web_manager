# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0012_auto_20171102_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_creation', models.DateField(auto_now_add=True)),
                ('record_update', models.DateField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('affected_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tagtype', to='dc_management.DC_Administrator')),
                ('affected_dcuser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tagtype', to='dc_management.DC_User')),
                ('affected_govdoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tagtype', to='dc_management.Governance_Doc')),
                ('affected_prj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tagtype', to='dc_management.Project')),
                ('affected_server', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tagtype', to='dc_management.Server')),
                ('affected_software', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tagtype', to='dc_management.Software')),
                ('affected_softwarelicensetype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tagtype', to='dc_management.Software_License_Type')),
            ],
        ),
        migrations.CreateModel(
            name='AlertTagType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='alerttag',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagtype', to='dc_management.AlertTagType'),
        ),
    ]
