# Generated by Django 5.0.3 on 2024-04-01 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appcoder', '0003_rename_abstract_publicaciones_autor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='Camada',
            new_name='camada',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='Apellido',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='Especialidad',
            new_name='especialidad',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='publicaciones',
            old_name='Autor',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='publicaciones',
            old_name='Materia',
            new_name='materia',
        ),
        migrations.RenameField(
            model_name='publicaciones',
            old_name='Titulo',
            new_name='titulo',
        ),
    ]