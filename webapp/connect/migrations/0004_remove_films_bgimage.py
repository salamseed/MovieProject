# Generated by Django 4.1.7 on 2023-04-05 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0003_films_bgimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='films',
            name='bgimage',
        ),
    ]
