# Generated by Django 3.1.2 on 2021-01-08 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0003_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='test',
        ),
    ]
