# Generated by Django 4.2 on 2024-10-24 00:30

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_familia_instrumento_familia_del_instrumento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumento',
            name='Nombre_Del_Instrumento',
            field=models.CharField(max_length=100, unique=True, validators=[api.models.validate_only_letters_and_spaces]),
        ),
    ]
