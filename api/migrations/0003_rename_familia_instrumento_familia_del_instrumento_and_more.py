# Generated by Django 4.2 on 2024-10-24 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_nickname_instrumento_familia_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instrumento',
            old_name='Familia',
            new_name='Familia_Del_Instrumento',
        ),
        migrations.RenameField(
            model_name='instrumento',
            old_name='Nombre_Instrumento',
            new_name='Nombre_Del_Instrumento',
        ),
    ]
