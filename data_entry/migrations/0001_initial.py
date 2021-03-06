# Generated by Django 3.1.2 on 2020-11-14 03:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather', models.CharField(max_length=100)),
                ('temperature', models.IntegerField()),
                ('driver', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('track', models.CharField(blank=True, max_length=100)),
                ('fast_lap', models.CharField(blank=True, max_length=100)),
                ('engine', models.CharField(blank=True, max_length=100)),
                ('software', models.FloatField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
