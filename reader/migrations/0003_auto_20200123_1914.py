# Generated by Django 3.0.2 on 2020-01-23 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0002_auto_20200123_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='user',
            new_name='reader',
        ),
    ]
