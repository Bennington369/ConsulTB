
from django.shortcuts import render,redirect
from perfil.forms import PerfilModelForm
from .models import Perfil,categoria
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def perfil(request):
    cate= categoria.objects.all()
    xd=Perfil()
    ps=Perfil.objects.all()


    if request.method == 'POST':
        tipo_id = categoria.objects.get(pk = request.POST['categ'])
        xd.usuario= User.objects.get(pk=request.POST['userxd'])
        xd.categoria= tipo_id 
        xd.nomEstable=request.POST['nombre']
        xd.descripcion_Estable=request.POST['descripcion']
        xd.sitio_web=request.POST['web'] 
        xd.telefono=request.POST['telefono']
        xd.latitud=request.POST['lat']
        xd.longitud=request.POST['lng']
        xd.whatsapp=request.POST['whats']
        xd.imagen= request.FILES.get('img')
        xd.entrada= request.POST['hora1']
        xd.salida= request.POST['hora2']
        

        xd.save()

        return redirect('inicio')

    return render(request, "perfil.html",{"cate":cate,"ps":ps})



