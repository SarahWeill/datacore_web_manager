# Generated by Django 2.0 on 2018-02-07 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0032_auto_20180130_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='wrapup_date',
            field=models.DateField(blank=True, null=True, verbose_name='date project close requested'),
        ),
        migrations.AddField(
            model_name='project',
            name='wrapup_ticket',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='ticket for request to complete'),
        ),
        migrations.AlterField(
            model_name='dcuagenerator',
            name='enddate',
            field=models.CharField(default='02/06/2019', max_length=32, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='dcuagenerator',
            name='startdate',
            field=models.CharField(default='02/06/2018', max_length=32, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('RU', 'Running'), ('CO', 'Completed'), ('SU', 'Suspended'), ('SD', 'Shutting down')], default='RU', max_length=2),
        ),
    ]
