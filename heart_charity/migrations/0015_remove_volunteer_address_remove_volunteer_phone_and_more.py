# Generated by Django 5.1 on 2024-09-05 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_charity', '0014_remove_volunteer_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='phone',
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
