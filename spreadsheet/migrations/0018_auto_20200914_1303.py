# Generated by Django 3.1.1 on 2020-09-14 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spreadsheet', '0017_auto_20200914_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dane_Arkusza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imie', models.CharField(max_length=127)),
                ('Nazwisko', models.CharField(max_length=127)),
                ('Email', models.CharField(blank=True, default=None, max_length=127, null=True)),
                ('Numer_telefonu', models.CharField(blank=True, default=None, max_length=127, null=True)),
                ('Adres', models.CharField(blank=True, default=None, max_length=127, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]