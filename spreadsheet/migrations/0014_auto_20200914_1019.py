# Generated by Django 3.1.1 on 2020-09-14 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spreadsheet', '0013_auto_20200914_1016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arkusze',
            options={'verbose_name_plural': 'Arkusze'},
        ),
        migrations.AlterModelOptions(
            name='danearkusza',
            options={'verbose_name_plural': 'DaneArkusza'},
        ),
    ]