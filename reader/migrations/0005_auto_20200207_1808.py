# Generated by Django 3.0.2 on 2020-02-07 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0004_auto_20200123_1924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='lastName',
            new_name='last_name',
        ),
    ]
