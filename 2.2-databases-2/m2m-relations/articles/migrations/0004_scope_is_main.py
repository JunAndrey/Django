# Generated by Django 4.1.2 on 2022-11-28 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_tag_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
