# Generated by Django 2.0 on 2018-03-03 04:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0041_auto_20180302_2209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='migrationlog',
            options={'verbose_name': 'Migration Log', 'verbose_name_plural': 'Migration Logs'},
        ),
        migrations.AddField(
            model_name='migrationlog',
            name='node_destination',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='migration_destination', to='dc_management.Server'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='migrationlog',
            name='node_origin',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='migration_origin', to='dc_management.Server'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='migrationlog',
            name='access_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='access confirmation date'),
        ),
        migrations.AlterField(
            model_name='migrationlog',
            name='data_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='data integrity confirmation date'),
        ),
        migrations.AlterField(
            model_name='migrationlog',
            name='envt_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='environment confirmation date'),
        ),
    ]
