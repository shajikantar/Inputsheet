# Generated by Django 2.2.6 on 2019-11-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ISheet', '0002_auto_20191108_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_is',
            name='pd_country',
            field=models.CharField(max_length=50),
        ),
    ]
