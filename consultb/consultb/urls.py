"""consultb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from aplicacion import views
from aplicacion.views import VRegistro,cerrar_sesion,logear
from perfil.urls import urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),   
    path('perfil/', include('perfil.urls')),
    path('',views.index, name='index'),
    path('categoria/',views.Categoria, name='categoria'),
    path('contacto/',views.contacto, name='contacto'),
    path('registro/',VRegistro.as_view(), name='registro'),
    path('logear',logear,name="logear"),
    path('muestraperfil/<int:id>',views.muestraperfil,name="muestraperfil"),
    path('resultados/',views.busqueda,name="busqueda"),
    path('categoriastodas/<int:categoria_id>',views.categoriass,name="categoriass"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/logout',views.cerrar_sesion,'logout'),
    path('inicioperfil/',views.inicioxd,name='inicio'),
    path('inicioperfil/borrar/<int:id>', views.borrar, name='borrar'),
	path('inicioperfil/borrando/<int:id>', views.borrando, name='borrando'),

   






]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)