# Generated by Django 4.2 on 2024-10-23 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_www', '0003_alter_osoba_data_dodania_alter_osoba_plec'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko']},
        ),
    ]
