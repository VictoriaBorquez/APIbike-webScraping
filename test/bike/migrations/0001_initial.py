# Generated by Django 4.2.1 on 2023-05-16 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('altitude', models.IntegerField()),
                ('ebikes', models.IntegerField()),
                ('has_ebikes', models.BooleanField()),
                ('last_updated', models.IntegerField()),
                ('normal_bikes', models.IntegerField()),
                ('payment', models.JSONField()),
                ('payment_terminal', models.BooleanField()),
                ('renting', models.IntegerField()),
                ('returning', models.IntegerField()),
                ('slots', models.IntegerField()),
                ('uid', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empty_slots', models.IntegerField()),
                ('free_bikes', models.IntegerField()),
                ('id_station', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('name', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
                ('extra', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bike.extra')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.JSONField()),
                ('gbfs_href', models.URLField()),
                ('href', models.CharField(max_length=100)),
                ('id_network', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bike.location')),
                ('stations', models.ManyToManyField(to='bike.station')),
            ],
        ),
    ]
