from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("anuncio/<int:id>", views.ver_anuncio, name="ver_anuncio"),
	path("anuncio/nuevo_anuncio", views.nuevo_anuncio, name="nuevo_anuncio"),
	path("anuncio/anuncio_nuevo", views.anuncio_nuevo, name="anuncio_nuevo"),
	path("contratista/<int:id>", views.ver_contratista, name="ver_contratista"),
	path("anuncio/<int:id>/comentar", views.comentar, name="comentar"),
	path("anuncio/<int:id>/borrar", views.borrar_anuncioT, name="borrar_anuncioT"),
	path("anuncio/search", views.search, name="search"),
	path("anuncio/<int:id>/calificar/<int:calificacion>/", views.calificar_anuncio, name="calificar_anuncio"),
	path("anuncio/ver_anuncios", views.ver_anuncios, name="ver_anuncios"),
	path("anuncio/<int:id>/editar", views.editar_anuncio, name = "editar_anuncio"),
	path("contratista/<int:id>/editar", views.editar_anuncioC, name = "editar_anuncioC"),
] 

