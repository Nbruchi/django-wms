# Generated by Django 5.1.2 on 2024-10-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='generated_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
