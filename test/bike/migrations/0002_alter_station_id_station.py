# Generated by Django 4.2.1 on 2023-05-16 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='id_station',
            field=models.CharField(max_length=200),
        ),
    ]
