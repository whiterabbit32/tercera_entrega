from django.db import models

# Create your models here.


class Curso (models.Model):
    nombre= models.CharField (max_length=40)
    camada= models.IntegerField ()



class Estudiante (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    email = models.EmailField()

    


class Profesor (models.Model):
    nombre = models.CharField (max_length= 35)
    apellido = models.CharField (max_length= 35)
    email= models.EmailField()
    especialidad= models.CharField( max_length=30)

class Publicaciones (models.Model):
    titulo= models.CharField (max_length =35)
    autor= models.CharField (max_length =35)
    materia= models.CharField (max_length =35)
    
    