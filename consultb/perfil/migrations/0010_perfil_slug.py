# Generated by Django 4.0.3 on 2022-05-29 21:17

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0009_perfil_entrada_perfil_salida'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='nomEstable'),
            preserve_default=False,
        ),
    ]
