# Generated by Django 4.0.4 on 2022-06-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_profile_experiance_profile_image_profile_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
