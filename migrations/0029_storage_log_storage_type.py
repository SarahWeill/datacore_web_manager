# Generated by Django 2.0 on 2018-01-18 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0028_auto_20180117_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='storage_log',
            name='storage_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dc_management.StorageCost'),
            preserve_default=False,
        ),
    ]
