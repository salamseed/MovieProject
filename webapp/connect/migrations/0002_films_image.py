# Generated by Django 4.1.7 on 2023-04-03 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='image',
            field=models.ImageField(default='abcd', upload_to='pics'),
            preserve_default=False,
        ),
    ]
