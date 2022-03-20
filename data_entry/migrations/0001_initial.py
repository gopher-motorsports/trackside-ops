# Generated by Django 3.1.2 on 2022-03-20 20:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('car_type', models.CharField(max_length=10)),
                ('is_dyno', models.BooleanField(default=False)),
                ('is_racespec', models.BooleanField(default=False)),
                ('driver', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('drive_day_lead', models.CharField(max_length=100)),
                ('track', models.CharField(blank=True, max_length=100)),
                ('weather', models.CharField(max_length=100)),
                ('air_temp', models.IntegerField()),
                ('track_temp', models.IntegerField()),
                ('tires', models.CharField(max_length=100)),
                ('tire_condition', models.CharField(max_length=100)),
                ('tire_serial_number', models.CharField(max_length=100)),
                ('engine', models.CharField(blank=True, max_length=100)),
                ('motor_num', models.CharField(max_length=100)),
                ('comments', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('subteam', models.CharField(max_length=100)),
                ('phone', models.CharField(default=0, max_length=100)),
                ('licensed', models.BooleanField(default=False)),
            ],
        ),
    ]
