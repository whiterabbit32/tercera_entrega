from django.shortcuts import render, redirect
from Appcoder.models import Curso, Profesor , Publicaciones, Estudiante
from Appcoder.forms import EstudianteForm, ProfesorForm, PublicacionesForm, CursoForm
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def inicio (request):
    return render (request , "padre.html")

def alta_curso (request):
    if request.method == 'POST':
        form = CursoForm (request.POST)
        if form.is_valid():
            datos= form.cleaned_data
            nuevo_curso= Curso ( nombre= datos["nombre"], promocion= datos["promocion"])
            nuevo_curso.save()
            respuesta= loader.get_template ("cursos.html")
            mensaje= "El curso ha sido agregado con exito a la base de datos"
            diccionario= {"mensaje": [mensaje]}
            documento= respuesta.render (diccionario)
            return HttpResponse (documento)
    else:
         return render(request, 'cursos.html')

def ver_curso (request):
    cursos= Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla= loader.get_template ('cursos.html')
    documento= plantilla.render (dicc)
    return HttpResponse (documento)







def registrar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm (request.POST)
        if form.is_valid():
            datos= form.cleaned_data
            nuevo_estudiante= Estudiante( nombre= datos["nombre"], apellido= datos["apellido"], email= datos["email"], dni= datos ["dni"])
            nuevo_estudiante.save()
            respuesta= loader.get_template ("registro.html")
            mensaje= "Bienvenido, ha sido registrado como alumno exitosamente"
            diccionario= {"mensaje": [mensaje]}
            documento= respuesta.render (diccionario)
            return HttpResponse (documento)
    else:
         return render(request, 'registro_estudiante.html')


def profesor (request):
     if request.method == 'POST':
        form = ProfesorForm (request.POST)
        if form.is_valid():
            datos= form.cleaned_data
            nuevo_Profe= Profesor( nombre= datos["nombre"], apellido= datos["apellido"], email= datos["email"], especialidad= datos ["especialidad"])
            nuevo_Profe.save()
            respuesta= loader.get_template ("profesores.html")
            mensaje= "Bienvenido profesor, ha sido registrado con éxito"
            diccionario= {"mensaje": [mensaje]}
            documento= respuesta.render (diccionario)
            
            return HttpResponse (documento)
     else:
         return render(request, 'profesores.html')
    


def ver_buscar_publicaciones (request):
    #if request.method == 'POST':
     #   form= PublicacionesForm (request.POST)
      #  if form.is_valid:
       #     datos= form.cleaned_data ['materia']
        #    busq_publicaciones= Publicaciones.objects.filter (materia__icontains="Materia")
         #   titulo= busq_publicaciones["titulo"]
          #  return render(request, 'resultado_busqueda.html', {'publicaciones': titulo})
    #else:
     #   form = PublicacionesForm()
    return render(request, 'busqueda_publicacion.html')

def buscar_publicaciones (request):
    if request.GET ["materia"]:
        materia= request.GET ["materia"]
        resultados= Publicaciones.objects.filter (materia__icontains= materia)
        return render (request, "resultado_busqueda.html", {"publicaciones": resultados} )

def registro (request):
    return render (request, "registro.html")

def nuevas_publicaciones (request):
     if request.method == 'POST':
        form = PublicacionesForm (request.POST)
        if form.is_valid():
            datos= form.cleaned_data
            nueva_publicacion= Publicaciones( titulo= datos["titulo"], autor= datos["autor"], materia= datos["materia"])
            nueva_publicacion.save()
            respuesta= loader.get_template ("publicacion.html")
            mensaje= f" el artículo ha sido registrado con éxito"
            diccionario= {"mensaje": [mensaje]}
            documento= respuesta.render (diccionario)
            return HttpResponse (documento)
     else:
         return render(request, 'publicacion.html') 

    

    #return render(
             #   request,
              #  "register.html",
               # {"error": ["Ocurrió un error al registrar el usuario."]},
           # )