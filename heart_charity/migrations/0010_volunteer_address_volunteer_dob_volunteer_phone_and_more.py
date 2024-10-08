# Generated by Django 5.1 on 2024-09-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_charity', '0009_remove_person_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='dob',
            field=models.DateField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='phone',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
