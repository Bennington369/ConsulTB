# Generated by Django 4.0.3 on 2022-05-28 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='latitud',
            field=models.DecimalField(decimal_places=20, max_digits=20),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='longitud',
            field=models.DecimalField(decimal_places=20, max_digits=20),
        ),
    ]
