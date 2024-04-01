from django.urls import path
from . import views

urlpatterns= [
    path ("alta_curso/<nombre>", views.alta_curso),
    path ("", views.inicio, name= "home"),
    path ("ver_curso/", views.ver_curso, name="cursos" ),
    path ("profesores", views.profesores, name= "profesores"),
    path ("registro", views.registro, name= "registro"),
    path ("profesores", views.profesores, name= "profesores"),
    path ("registrar_estudiante", views.registrar_estudiante, name= "registrar estudiante"),
    path ("ver_buscar_publicaciones", views.ver_buscar_publicaciones, name= "ver_buscar_publicaciones"),
    path ("publicacion", views.nuevas_publicaciones, name= "publicacion"),
    path ("buscar_publicaciones", views.buscar_publicaciones)
]