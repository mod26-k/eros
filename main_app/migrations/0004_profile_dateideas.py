# Generated by Django 4.2 on 2023-05-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_dateideas_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dateideas',
            field=models.ManyToManyField(to='main_app.dateideas'),
        ),
    ]