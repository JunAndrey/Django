# Generated by Django 4.1.2 on 2022-12-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_measurements_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurements',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]