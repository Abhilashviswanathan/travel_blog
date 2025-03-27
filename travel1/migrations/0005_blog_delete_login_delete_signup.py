# Generated by Django 5.1.2 on 2024-11-21 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel1', '0004_rename_name_signup_username_login_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=500)),
                ('photos', models.ImageField(default='', upload_to='photos')),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
        migrations.DeleteModel(
            name='signup',
        ),
    ]
