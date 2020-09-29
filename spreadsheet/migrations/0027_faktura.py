# Generated by Django 3.1.1 on 2020-09-29 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spreadsheet', '0026_auto_20200925_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faktura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kwota_faktury', models.IntegerField()),
                ('Data_wystawienia', models.DateField()),
                ('Opłacona', models.BooleanField()),
                ('Klient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='klient', to='spreadsheet.danearkusza')),
                ('Sprzedawca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sprzedawca', to='spreadsheet.danearkusza')),
            ],
        ),
    ]