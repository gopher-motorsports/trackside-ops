# Generated by Django 3.1.2 on 2021-01-08 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0006_auto_20210107_2350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='people',
            new_name='personnel',
        ),
    ]