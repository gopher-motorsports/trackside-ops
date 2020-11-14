# Generated by Django 3.1.2 on 2020-11-09 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='driver',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='test',
            name='engine',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='test',
            name='fast_lap',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='test',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='test',
            name='track',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='test',
            name='weather',
            field=models.CharField(max_length=100),
        ),
    ]
