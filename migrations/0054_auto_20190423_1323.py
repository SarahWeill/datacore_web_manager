# Generated by Django 2.1.4 on 2019-04-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dc_management', '0053_auto_20190423_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectbillingrecord',
            name='storage_expense',
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='base_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='base_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='db_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='db_setup',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='db_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='hosting_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='hosting_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_1_expense',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_1_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_1_type',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_1_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_2_expense',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_2_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_2_type',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_2_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_3_expense',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_3_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_3_type',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_3_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_4_expense',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_4_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_4_type',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='storage_4_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='sw_rates',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectbillingrecord',
            name='sw_value',
            field=models.TextField(blank=True, null=True),
        ),
    ]
