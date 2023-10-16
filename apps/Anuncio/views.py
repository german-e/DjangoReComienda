from django.shortcuts import render, redirect
from .models import Anuncio_Trans, Contratista,Localidad,Transporte, Comentario , CalificacionPost
from .forms import AnuncioForm, ContratistaForm, ComentarioForm, LocalidadForm, TransporteForm,SearchForm, EditarAnuncioTForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    if request.GET:
        search_form = SearchForm(request.GET)
    else:
        search_form = SearchForm()

    filtro_titulo = request.GET.get("titulo", "")
    filtro_localidad = request.GET.get("localidad", "")
    orden_anuncio = request.GET.get("orden", None)
    lista_anuncio = Anuncio_Trans.objects.filter(titulo__icontains = filtro_titulo).filter(localidad_destino__localidad__icontains=filtro_localidad)
    lista_contrato = Contratista.objects.filter(titulo__icontains = filtro_titulo).filter(localidad_destino__localidad__icontains=filtro_localidad)
    #localidades = Localidad.objects.filter(localidad__icontains = filtro_localidad)
    
    if orden_anuncio == "titulo":
        lista_anuncio= lista_anuncio.order_by("titulo")
        lista_contrato= lista_contrato.order_by("titulo")
    elif orden_anuncio == "localidad":
        lista_anuncio= lista_anuncio.order_by("localidad_destino")
        lista_contrato= lista_contrato.order_by("localidad_destino")
    elif orden_anuncio == "antiguo":
        lista_anuncio= lista_anuncio.order_by("fecha_publicacion")
        lista_contrato= lista_contrato.order_by("fecha_viaje")
    elif orden_anuncio == "nuevo":
        lista_anuncio= lista_anuncio.order_by("-fecha_publicacion")
        lista_contrato= lista_contrato.order_by("-fecha_viaje")


    contexto={ 
    "lista_anuncio" : lista_anuncio,
    "lista_contrato": lista_contrato,
    #"localidades": localidades,
    "search_form":search_form,

    }
    return render(request, "anuncio/index.html", contexto)

def ver_anuncio(request,id):
    anuncio = Anuncio_Trans.objects.get(pk=id)
    usuario = anuncio.usuario
    lista_anuncio = Anuncio_Trans.objects.filter(usuario_id=usuario.id)
    form_comentario = ComentarioForm()
    comentarios = anuncio.comentario_set.all().order_by("-fecha_creacion")
    contexto = {
    "anuncio" : anuncio,
    "lista_anuncio" : lista_anuncio,
    "form_comentario": form_comentario,
    "comentarios":comentarios,
    }
    return render(request, "anuncio/ver_transportista.html",contexto)

def ver_contratista(request,id):
    anuncio = Contratista.objects.get(pk=id)
    usuario = anuncio.usuario
    lista_anuncio = Contratista.objects.filter(usuario_id=usuario.id)
    form_comentario = ComentarioForm()
    contexto = {
    "anuncio" : anuncio,
    "lista_anuncio" : lista_anuncio,
    "form_comentario": form_comentario
    }
    return render(request, "anuncio/ver_contratista.html",contexto)

#Transportista
@login_required
def nuevo_anuncio(request):
    if request.method == "POST":
        form=AnuncioForm(request.POST)
        if form.is_valid():
            anuncio=form.save(commit=False)
            anuncio.usuario = request.user
            anuncio.save()
            return redirect("ver_anuncio", anuncio.id)
        else:
            contexto={"form":form}
            return render(request, "anuncio/nuevo_anuncio.html", contexto)
    form=AnuncioForm()
    contexto={"form":form}
    return render(request, "anuncio/nuevo_anuncio.html", contexto)

#Contratista
@login_required
def anuncio_nuevo(request):
    if request.method == "POST":
        form=ContratistaForm(request.POST)
        if form.is_valid():
            anuncio=form.save(commit=False)
            anuncio.usuario = request.user
            anuncio.save()
            return redirect("ver_contratista", anuncio.id)
        else:
            contexto={"form":form}
            return render(request, "anuncio/anuncio_nuevo.html", contexto)
    form=ContratistaForm()
    contexto={"form":form}
    return render(request, "anuncio/anuncio_nuevo.html", contexto)

@login_required
def comentar(request,id):
    anuncio = Anuncio_Trans.objects.get(pk=id)
    if anuncio.permitir_comentarios:
        if request.method == "POST":
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.usuario = request.user
                comentario.anuncio = anuncio
                comentario.save()
                return redirect("ver_anuncio", anuncio.id)
    else:
        return redirect("ver_anuncio", anuncio.id)


@login_required
def borrar_anuncioT(request,id):
    anuncio = Anuncio_Trans.objects.get(pk=id)
    if request.method == "POST":
        if anuncio.usuario == request.user:
            anuncio.delete()
            return redirect("ver_perfil", request.user.id)


def search(request): 
    if request.GET:
        search_form = SearchForm(request.GET)
    else:
        search_form = SearchForm()

    filtro_titulo = request.GET.get("titulo", "")
    filtro_localidad = request.GET.get("localidad", "")
    orden_anuncio = request.GET.get("orden", None)
    lista_anuncio = Anuncio_Trans.objects.filter(titulo__icontains = filtro_titulo).filter(localidad_destino__localidad__icontains=filtro_localidad)
    lista_contrato = Contratista.objects.filter(titulo__icontains = filtro_titulo).filter(localidad_destino__localidad__icontains=filtro_localidad)
    #localidades = Localidad.objects.filter(localidad__icontains = filtro_localidad)
    
    if orden_anuncio == "titulo":
        lista_anuncio= lista_anuncio.order_by("titulo")
        lista_contrato= lista_contrato.order_by("titulo")
    elif orden_anuncio == "localidad":
        lista_anuncio= lista_anuncio.order_by("localidad_destino")
        lista_contrato= lista_contrato.order_by("localidad_destino")
    elif orden_anuncio == "antiguo":
        lista_anuncio= lista_anuncio.order_by("fecha_publicacion")
        lista_contrato= lista_contrato.order_by("fecha_viaje")
    elif orden_anuncio == "nuevo":
        lista_anuncio= lista_anuncio.order_by("-fecha_publicacion")
        lista_contrato= lista_contrato.order_by("-fecha_viaje")
    contexto={ 
    "lista_anuncio" : lista_anuncio,
    "lista_contrato": lista_contrato,
    #"localidades": localidades,
    "search_form":search_form,
    }

    return render(request, "anuncio/search.html", contexto)

@login_required
def calificar_anuncio(request, id, calificacion):
    perfil = request.user
    anuncio = Anuncio_Trans.objects.get(pk=id)
    calif = perfil.detalle_calificacion.filter(anuncio=anuncio).first()

    if calif:
        calif.calificacion = calificacion
    else:
        calif = CalificacionPost()
        calif.anuncio = anuncio
        calif.calificacion = calificacion
        calif.usuario = perfil

    try:
        calif.full_clean() 
        calif.save()
    except Exception as ex: 
        return HttpResponse("error")
    return redirect("ver_anuncio", anuncio.id)

@login_required
def ver_anuncios(request):
    if request.GET:
        search_form = SearchForm(request.GET)
    else:
        search_form = SearchForm()

    filtro_titulo = request.GET.get("titulo", "")
    filtro_localidad = request.GET.get("localidad", "")
    orden_anuncio = request.GET.get("orden", None)
    lista_anuncio = Anuncio_Trans.objects.filter(titulo__icontains = filtro_titulo).filter(localidad_destino__localidad__icontains=filtro_localidad)
    lista_contrato = Contratista.objects.filter(titulo__icontains = filtro_titulo).filter(localidad_destino__localidad__icontains=filtro_localidad)
    #localidades = Localidad.objects.filter(localidad__icontains = filtro_localidad)
    
    if orden_anuncio == "titulo":
        lista_anuncio= lista_anuncio.order_by("titulo")
        lista_contrato= lista_contrato.order_by("titulo")
    elif orden_anuncio == "localidad":
        lista_anuncio= lista_anuncio.order_by("localidad_destino")
        lista_contrato= lista_contrato.order_by("localidad_destino")
    elif orden_anuncio == "antiguo":
        lista_anuncio= lista_anuncio.order_by("fecha_publicacion")
        lista_contrato= lista_contrato.order_by("fecha_viaje")
    elif orden_anuncio == "nuevo":
        lista_anuncio= lista_anuncio.order_by("-fecha_publicacion")
        lista_contrato= lista_contrato.order_by("-fecha_viaje")

    contexto={ 
    "lista_anuncio" : lista_anuncio,
    "lista_contrato": lista_contrato,
    #"localidades": localidades,
    "search_form":search_form,

    }
    return render(request,"anuncio/ver_anuncios.html", contexto)

@login_required
def editar_anuncio(request,id):
    anuncio = Anuncio_Trans.objects.get(pk=id)
    print(anuncio)    
    if request.method == "GET":
        form = EditarAnuncioTForm(instance=anuncio)
        print(form)
        
    elif request.method == "POST":
        form = EditarAnuncioTForm(data=request.POST, instance=anuncio)
        if form.is_valid():
            anuncio = form.save()
            return redirect("ver_anuncio", anuncio.id)
    

    return render(request, "anuncio/editar_anuncio.html",{"form":form})


def editar_anuncioC(request,id):
    anuncio = Contratista.objects.get(pk=id)
    print(anuncio)    
    if request.method == "GET":
        form = EditarAnuncioTForm(instance=anuncio)
        print(form)
        
    elif request.method == "POST":
        form = EditarAnuncioTForm(data=request.POST, instance=anuncio)
        if form.is_valid():
            anuncio = form.save()
            return redirect("ver_anuncio", anuncio.id)
    

    return render(request, "anuncio/editar_anuncio.html",{"form":form})
