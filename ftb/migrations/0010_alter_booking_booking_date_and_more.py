# Generated by Django 4.2.2 on 2023-06-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftb', '0009_flight_flight_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_date',
            field=models.DateField(),
        ),
    ]
