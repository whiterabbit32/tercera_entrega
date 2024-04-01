from django import forms
from Appcoder.models import Curso, Estudiante, Profesor, Publicaciones

class EstudianteForm(forms.Form):
    nombre= forms.CharField (max_length=35)
    apellido= forms.CharField (max_length= 35)
    email= forms.EmailField ()
    dni= forms.CharField (max_length= 10)
        

class CursoForm(forms.Form):
    nombre= forms.CharField (max_length= 35)
    promocion= forms.IntegerField ()
    
        
        

class ProfesorForm(forms.Form):
    nombre= forms.CharField (max_length= 35)
    apellido= forms.CharField (max_length= 35)
    email= forms.CharField (max_length= 35)
    especialidad= forms.CharField (max_length= 35)
       

class PublicacionesForm(forms.Form):
    titulo= forms.CharField (max_length=35)
    autor=forms.CharField (max_length= 35)
    materia= forms.CharField (max_length=35)
