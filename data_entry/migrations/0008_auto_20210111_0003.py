# Generated by Django 3.1.2 on 2021-01-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0007_auto_20210107_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='personnel',
            field=models.CharField(default='Adrian', max_length=200),
            preserve_default=False,
        ),
    ]
