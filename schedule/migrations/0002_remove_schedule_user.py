# Generated by Django 5.1.2 on 2024-11-25 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='user',
        ),
    ]
