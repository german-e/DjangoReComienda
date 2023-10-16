from django import forms
from .models import Anuncio_Trans, Contratista, Localidad, Transporte, Comentario

class LocalidadForm(forms.ModelForm):
    class Meta:
        model=Localidad
        fields="__all__"

class TransporteForm(forms.ModelForm):
    class Meta:
        model=Transporte
        fields="__all__"


class AnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio_Trans
        fields = "__all__"
        exclude = ('usuario',)
    
    def __init__(self, *args, **kwargs):
        super(AnuncioForm, self).__init__(*args, **kwargs)
        self.fields["permitir_comentarios"].widget.attrs.update({"type":"checkbox", "checked":"checked"})
        self.fields['fecha_caducidad'].widget.attrs.update({ 'class' : 'input-field col s12','placeholder' : 'ingrese fecha', 'type' : 'date'})
        """
        self.fields['nombre'].widget.attrs.update({'id' :  'name_input','placeholder' : 'ingrese nombre', 'type' : 'text'})
        self.fields['Email'].widget.attrs.update({'id' : 'email_input','placeholder' : 'ingrese email', 'type' : 'email'})
        self.fields['localidad_origen'].widget.attrs.update({'id' : 'subject_input' , 'placeholder' :'ingrese localidad origen','type' : 'subject_line'})
        self.fields['localidad_destino'].widget.attrs.update({'id' : 'subject_input' , 'placeholder' :'ingrese localidad destino', 'type' : ''})
        self.fields['recorrido'].widget.attrs.update({'class' : '','placeholder' : 'ingrese recorrido', 'type' : 'text'})
        self.fields['titulo'].widget.attrs.update({'class' :  'validate', 'placeholder': 'titulo', 'type' : 'text'})
        self.fields["descripcion"].widget.attrs.update({'message_input' : 'materialize-textarea','placeholder' : 'descripcion', 'type' : 'text'})
        self.fields['transporte'].widget.attrs.update({'class' : '' , 'placeholder' :'ingrese localidad destino', 'type' : ''})
        self.fields['fecha_caducidad'].widget.attrs.update({ 'class' : 'input-field col s12','placeholder' : 'ingrese fecha', 'type' : 'date'})
        self.fields['tel'].widget.attrs.update({'class' : 'telephone','placeholder' : 'tel', 'type' : 'number'})
"""
class ContratistaForm(forms.ModelForm):
    class Meta:
        model = Contratista
        fields = "__all__"
        exclude = ('usuario',"permitir_comentarios")

    """def __init__(self, *args, **kwargs):
        super(ContratistaForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update({'class' :  'validate', 'placeholder': 'titulo', 'type' : 'text'})
        self.fields['fecha_viaje'].widget.attrs.update({ 'class' : 'input-field col s12','placeholder' : 'ingrese fecha', 'type' : 'date'})"""


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('texto',)


class SearchForm(forms.Form):
    titulo = forms.CharField(max_length=30, required = False)
    localidad_destino = forms.CharField(max_length=50, required = False)
    ORDER_OPCIONES = (
        ("titulo", "Titulo"),
        ("localidad", "localidad"),
        ("Fecha",(
            ("antiguo", "Antiguo"),
            ("nuevo", "Nuevo"))
        ))
    orden = forms.ChoiceField(choices=ORDER_OPCIONES, required = False,
        initial="nuevo")

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields["titulo"].widget.attrs["placeholder"] = "Ingrese filtros titulo"
        self.fields["localidad_destino"].widget.attrs["placeholder"] = "Ingrese filtros localidad"


class EditarAnuncioTForm(forms.ModelForm):
    class Meta:
        model = Anuncio_Trans
        fields = ('nombre', 'E_mail', 'telefono', 'titulo', 'recorrido', 'descripcion', 'localidad_origen', 'localidad_destino','fecha_caducidad','permitir_comentarios',)

    def __init__(self, *args, **kwargs):
        super(EditarAnuncioTForm, self).__init__(*args, **kwargs)
        self.fields["permitir_comentarios"].widget.attrs.update({"type":"checkbox", "checked":"checked"})