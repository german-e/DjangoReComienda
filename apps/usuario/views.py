from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from .forms import NuevoUsuarioForm, EditarPerfilForm
from django.contrib.auth.decorators import login_required
from .models import Perfil
# Create your views here.
def bienvenido(request):
	return render(request, "usuario/bienvenido.html",{})


def nuevo_usuario(request):
	form = NuevoUsuarioForm()
	if request.method == "POST":
		form = NuevoUsuarioForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			if user is not None:
				login(request,user)
				return redirect("index")
	return render(request, "usuario/nuevo_usuario.html",{"form": form})	

def iniciar_sesion(request):
	form = AuthenticationForm()
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				return redirect("index")
	return render(request, "usuario/iniciar_sesion.html", {"form":form})



@login_required
def editar_perfil(request):
    perfil = request.user
    form = EditarPerfilForm(instance = perfil)
    if request.method == "POST":
        form = EditarPerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            perfil = form.save()
            return redirect("ver_perfil", perfil.id)
    return render(request, "usuario/editar_perfil.html",{"form":form, "perfil":perfil})



@login_required
def cerrar_sesion(request):
	logout(request)
	return redirect("index")
@login_required
def ver_perfil(request,id):
    perfil = Perfil.objects.get(pk=id)
    contexto = {
        "perfil":perfil,
        }
    template = "usuario/perfil.html"
    return render(request, template, contexto)

@login_required
def borrar_perfil(request, id):

        u = Perfil.objects.get(pk = id)

        if request.method == "POST":
        	try:
        		
        		u.delete()       		
        		return redirect('index')               
        	except ex:
        		return redirect('ver_perfil')
        		
        return render(request, 'usuario/borrar_perfil.html')