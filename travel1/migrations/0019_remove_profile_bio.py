# Generated by Django 5.1.2 on 2024-11-27 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel1', '0018_alter_blogmodel_travel_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
