# Generated by Django 4.2.2 on 2023-06-23 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ftb', '0006_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
