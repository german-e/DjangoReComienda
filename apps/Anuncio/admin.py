  
from django.contrib import admin
from .models import Anuncio_Trans, Contratista, Localidad, Transporte, Comentario
# Register your models here.
admin.site.register(Anuncio_Trans)
admin.site.register(Contratista)
admin.site.register(Localidad)
admin.site.register(Transporte)
admin.site.register(Comentario)