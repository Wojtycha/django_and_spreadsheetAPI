# Generated by Django 3.1.1 on 2020-09-11 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spreadsheet', '0003_auto_20200911_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sheets',
            old_name='title',
            new_name='cell1',
        ),
        migrations.RenameField(
            model_name='sheets',
            old_name='liczba',
            new_name='cell2',
        ),
    ]
