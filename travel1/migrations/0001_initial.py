# Generated by Django 5.1.2 on 2024-11-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='singup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
