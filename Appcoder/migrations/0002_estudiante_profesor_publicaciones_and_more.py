# Generated by Django 5.0.3 on 2024-03-31 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appcoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=35)),
                ('Apellido', models.CharField(max_length=35)),
                ('Email', models.EmailField(max_length=254)),
                ('Especialidad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=35)),
                ('Abstract', models.CharField(max_length=35)),
                ('Materia', models.CharField(max_length=35)),
            ],
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='camada',
            new_name='Camada',
        ),
        migrations.RenameField(
            model_name='curso',
            old_name='nombre',
            new_name='Nombre',
        ),
    ]
