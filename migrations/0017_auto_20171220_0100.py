# Generated by Django 2.0 on 2017-12-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0016_auto_20171130_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='status',
            field=models.CharField(choices=[('ON', 'On'), ('OF', 'Off'), ('DE', 'Decommissioned')], default='ON', max_length=2),
        ),
    ]
