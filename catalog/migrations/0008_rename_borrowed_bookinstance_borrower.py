# Generated by Django 3.2.3 on 2021-05-19 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_rename_borrower_bookinstance_borrowed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinstance',
            old_name='borrowed',
            new_name='borrower',
        ),
    ]
