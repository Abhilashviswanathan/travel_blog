# Generated by Django 5.1.2 on 2024-11-27 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel1', '0019_remove_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics/'),
        ),
    ]
