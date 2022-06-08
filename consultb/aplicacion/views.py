from this import d
from django.shortcuts import render, redirect
from django.http import HttpResponse
from aplicacion.forms import UsuarioNuevo
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from perfil.models import categoria,Perfil
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'index.html')

def Categoria(request):
    cate= categoria.objects.all()
    return render(request,'web/categorias.html',{"cate":cate})

def categoriass(request,categoria_id):   
    ctg = categoria.objects.get(id=categoria_id)
    tiendas=Perfil.objects.filter(categoria=ctg)
    return render(request,'web/busqueda_cate.html',{'ctg':ctg,'tiendas':tiendas})

def contacto(request):
    return render(request,'web/contacto.html')

class VRegistro(View):
    def get(self, request):
       form = UsuarioNuevo()
       return render(request,'web/registro.html',{"form":form})
    
    def post(self, request):
        form = UsuarioNuevo(request.POST)

        if form.is_valid():
            usuario=form.save()
            login(request,usuario)
            return redirect('perfil')

        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            
            return render(request,'web/registro.html',{"form":form})
            
def cerrar_sesion(request):
    logout(request)
    return render(request,"index.html")

def logear(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuarioingreso = authenticate(username=nombre,password=contra)
            if usuarioingreso is not None:
                login(request,usuarioingreso)
                return redirect('inicio')
            else:
                messages.error(request,"Usuario o contraseña no correcto")
        else:
            messages.error(request,"Usuario o contraseña no correcto")

    form=AuthenticationForm()
    return render(request,'registration/login.html',{"form":form})




def muestraperfil(request,id):
    if Perfil.objects.filter(id=id).exists():    
        per=Perfil.objects.get(id=id)
        return render(request,"web/perfil_cliente.html",{"per":per})

def busqueda(request):
    tiendas=Perfil.objects.all()
    busc= request.GET.get('prd').upper()
    
    if busc != '' and busc is not None:       
        tiendas=Perfil.objects.filter(Q(nomEstable__upper__contains=(busc))|Q(telefono__icontains=busc))
        
        return render(request,"web/busqueda.html",{"tiendas":tiendas, "query":busc})
    else:
        mensaje= "No has introducido nada"  
    
    return render(request, 'web/busqueda.html',{"mensaje":mensaje})

@login_required
def inicioxd(request):

     perfiles= Perfil.objects.all().filter(usuario_id=request.user)
     return render(request,"inicio.html",{"perfiles":perfiles})

def borrar(request, id):
	perfil = Perfil.objects.get(id=id)
	return render(request, 'web/borrar.html', {'perfil':perfil })

def borrando(request, id):
	perfil = Perfil.objects.get(id=id)
	perfil.delete()
	return redirect('inicio')