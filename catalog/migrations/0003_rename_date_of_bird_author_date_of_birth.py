# Generated by Django 3.2.3 on 2021-05-18 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210517_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='date_of_bird',
            new_name='date_of_birth',
        ),
    ]