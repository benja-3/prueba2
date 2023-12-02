"""
URL configuration for EncuentratuFuturo2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from EncuentraTuFuturoApp.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name='inicio'),
    path('quienes_somos/',quienes_somos, name='quienes_somos'),
    path('carreras/', carreras, name='carreras'),
    path('eliminarCarrera/<int:IdCarrera>/', eliminarCarrera, name="eliminarCarrera"),
    path('editarC/<int:idcarrera>/', editarCarrera, name='editarC'),
    path('eliminarIntitucion/<int:idinstitucion>/', eliminarIntitucion, name="eliminarIntitucion"),
    path('instituciones/', instituciones, name="instituciones"),
    path('editarInstitucion/<int:idinstitucion>/', editarInstitucion, name='editarInstitucion'),
    path('registro/',registro, name='registro'),
    path('ingresoadm/',registroadministrador,name='ingresoadm'),  
    path('Login/',loginusuarios,name='login'),
    path('Loginadm/',loginadministrador,name='loginadm'),
    path('cerrarcu/',cerrarsesionusuario,name='cerrarUsuario'),
    path('cerrarca/',cerrarsesionadministrador,name='cerrarAdministrador'),    
    path('creari/',crearIntritucion,name='crearInstitucion'),
    path('crearC/',CrearCarrera, name="CrearCarrera"),
    path('agregar_favorito/',agregar_favorito,name="agregar_favorito")
]
