# Generated by Django 5.0.3 on 2024-04-01 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appcoder', '0002_estudiante_profesor_publicaciones_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicaciones',
            old_name='Abstract',
            new_name='Autor',
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='dni',
            field=models.CharField(max_length=10),
        ),
    ]
