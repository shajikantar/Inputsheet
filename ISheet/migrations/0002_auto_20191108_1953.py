# Generated by Django 2.2.6 on 2019-11-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ISheet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='form_IS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pd_country', models.CharField(choices=[('1', 'India'), ('2', 'China')], max_length=100)),
                ('pd_methodology', models.CharField(max_length=4)),
                ('pd_Plat_methodology', models.CharField(max_length=10)),
                ('pd_FW', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Is_details',
        ),
    ]
