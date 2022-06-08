from django import forms
from .models import Perfil,categoria
#clase para la generación de un formulario de la clase Alumno
#con los campos num_contro,nombre, paterno, materno,semestre, carrera
class PerfilModelForm(forms.ModelForm):
    cate = forms.ModelChoiceField(queryset=categoria.objects.all(),     empty_label="Seleccione una categoria")
    nomEstable = forms.CharField(label="Número de Control:")
    descripcion_Estable= forms.CharField()
    sitio_web= forms.URLField()
    latitud	= forms.CharField()
    longitud= forms.CharField()
    telefono= forms.CharField()
    whatsapp= forms.CharField()
    imagen	= forms.ImageField()

    cate.widget.attrs.update({'class': 'form-select'})
    nomEstable.widget.attrs.update({'class': 'form-control'})
    descripcion_Estable.widget.attrs.update({'class': 'form-control'})
    sitio_web.widget.attrs.update({'class': 'form-control'})
    latitud.widget.attrs.update({'class': 'form-control'})
    longitud.widget.attrs.update({'class': 'form-select'})
    telefono.widget.attrs.update({'class': 'form-control'})
    whatsapp.widget.attrs.update({'class': 'form-control'})
    imagen.widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model  = Perfil
        fields = [
			'cate', 'nomEstable', 'descripcion_Estable', 'sitio_web', 'latitud', 'longitud','telefono','whatsapp','imagen'
		]
#clase para la generación de un formulario
class PerfilForm(forms.Form):
    cate = forms.ModelChoiceField(queryset=categoria.objects.all(),     empty_label="Seleccione una categoria")
    nomEstable = forms.CharField(label="Número de Control:")
    descripcion_Estable= forms.CharField()
    sitio_web= forms.URLField()
    latitud	= forms.CharField()
    longitud= forms.CharField()
    telefono= forms.CharField()
    whatsapp= forms.CharField()
    imagen	= forms.ImageField()

    cate.widget.attrs.update({'class': 'form-select'})
    nomEstable.widget.attrs.update({'class': 'form-control'})
    descripcion_Estable.widget.attrs.update({'class': 'form-control'})
    sitio_web.widget.attrs.update({'class': 'form-control'})
    latitud.widget.attrs.update({'class': 'form-control'})
    longitud.widget.attrs.update({'class': 'form-select'})
    telefono.widget.attrs.update({'class': 'form-control'})
    whatsapp.widget.attrs.update({'class': 'form-control'})
    imagen.widget.attrs.update({'class': 'form-control'})