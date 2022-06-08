

from distutils.command.upload import upload
from django.db import models
from django.db.models import Transform
from django.db.models import CharField
from django.contrib.auth.models import User
# Create your models here.

class UpperCase(Transform):
     lookup_name = 'upper'
     function = 'UPPER'
     bilateral = True

CharField.register_lookup(UpperCase)

class categoria(models.Model):
     nombre = models.CharField(max_length= 50)

     def __str__(self):
          return self.nombre
     
   
class Perfil(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE, related_name='perfiles')
    categoria = models.ForeignKey(categoria,on_delete=models.PROTECT)  
    nomEstable = models.CharField(max_length= 50,null=False,blank=False)
    descripcion_Estable = models.CharField(max_length= 250,null=False,blank=False)
    sitio_web = models.URLField(max_length= 200,null=True,blank=True)
    latitud = models.CharField(max_length=25,null=False,blank=False)
    longitud = models.CharField(max_length=25,null=False,blank=False)
    telefono = models.CharField(max_length= 10,null=True,blank=True)
    whatsapp= models.CharField(max_length= 10, null=True,blank=True)
    imagen= models.ImageField(upload_to="perfiles",null=False)
    entrada= models.CharField(max_length= 20,null=False,blank=False)
    salida= models.CharField(max_length= 20,null=False,blank=False)
   

    def nombre(self):
         return "{} - {}".format(self.nomEstable,self.telefono)
     
    def __str__(self):
         return self.nombre()

