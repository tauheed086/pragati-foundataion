# Generated by Django 5.1 on 2024-09-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_charity', '0016_volunteer_dob_volunteer_gender_volunteer_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dependent',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
