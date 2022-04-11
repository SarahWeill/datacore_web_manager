# Generated by Django 3.2 on 2021-11-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0073_auto_20211117_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='servers',
            field=models.ManyToManyField(related_name='project_servers', to='dc_management.Server'),
        ),
    ]
