# Generated by Django 5.1 on 2024-09-16 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heart_charity', '0024_alter_eventimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='phone',
        ),
    ]
