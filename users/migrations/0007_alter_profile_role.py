# Generated by Django 5.1.2 on 2024-10-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('customer', 'Customer'), ('admin', 'Admin'), ('staff', 'Staff')], default='customer', max_length=20),
        ),
    ]