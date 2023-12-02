from django.db import models
from django.db.models.fields import CharField, URLField

# Create your models here.

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    Contraseña=models.TextField(max_length=30)

class administrador(models.Model):
    idAdministrador = models.AutoField(primary_key=True)
    Nombreadm = models.CharField(max_length=30)
    Apellidoadm = models.CharField(max_length=30)
    correoadm = models.CharField(max_length=30)
    Contraseñaadm=models.TextField(max_length=30)

class Institucion(models.Model):
    idinstitucion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    region = models.CharField(max_length=25)
    informacion = models.CharField(max_length= 50)
    url = URLField(blank=True)

class Carrera(models.Model):
    idcarrera = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    Arancel = models.PositiveIntegerField(null=True, blank=True)
    Duracion =models.CharField(max_length=2)
    idinstitucion = models.ForeignKey(Institucion,null=False,on_delete=models.CASCADE)

class Favorito(models.Model):
    idfavorito = models.AutoField(primary_key=True)
    IdCarrera = models.ForeignKey(Carrera,null=False,on_delete=models.CASCADE)
    IdUsuario = models.ForeignKey(Usuario,null=False,on_delete=models.CASCADE)

  
