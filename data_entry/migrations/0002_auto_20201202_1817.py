# Generated by Django 3.1.2 on 2020-12-03 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='tire_condition',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='tires',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
