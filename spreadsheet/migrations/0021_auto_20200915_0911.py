# Generated by Django 3.1.1 on 2020-09-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spreadsheet', '0020_auto_20200914_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danearkusza',
            name='Numer_telefonu',
            field=models.CharField(blank=True, default=None, max_length=9, null=True),
        ),
    ]
