# Generated by Django 4.1.7 on 2023-04-04 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0002_films_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='bgimage',
            field=models.ImageField(default='dcba', upload_to='pics'),
            preserve_default=False,
        ),
    ]
