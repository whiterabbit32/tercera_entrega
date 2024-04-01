from django.urls import path
from . import views

urlpatterns= [
   
    path ("", views.inicio, name= "home"),
    path ("cursos", views.alta_curso, name="cursos" ),
    path ("profesor", views.profesor, name= "profesor"),
    path ("registro", views.registro, name= "registro"),
    path ("registrar_estudiante", views.registrar_estudiante, name= "registrar estudiante"),
    path ("ver_buscar_publicaciones", views.ver_buscar_publicaciones, name= "ver_buscar_publicaciones"),
    path ("publicacion", views.nuevas_publicaciones, name= "publicacion"),
    path ("buscar_publicaciones", views.buscar_publicaciones)
]