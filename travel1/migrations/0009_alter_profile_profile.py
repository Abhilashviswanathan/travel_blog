# Generated by Django 5.1.2 on 2024-11-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel1', '0008_remove_profile_image_profile_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
