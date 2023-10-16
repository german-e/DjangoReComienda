from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Perfil

class NuevoUsuarioForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields = ("first_name","last_name","username", "email", "password1",
         "password2","foto","telefono")

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        lista=["Nombre","Apellido","Usuario","Email","contraseña","repetir contraseña","telefono"]
        for x,valor in enumerate(self.fields):
            self.fields[valor].widget.attrs.update({'class' : 'validate','placeholder' : lista[x], 'type' : 'text'})
            if x==len(lista)-1:
                break
        self.fields["foto"].widget.attrs.update({'class' : 'texto-rojo','placeholder' : '', 'name':'foto' , 'accept':'image/*'})

class EditarPerfilForm(UserChangeForm):
    password = None
    class Meta:
        model = Perfil
        fields = ["username","first_name","last_name", "telefono", "email", "foto"]
        widget = {"username":forms.TextInput(attrs={"readonly":"readonly"})}