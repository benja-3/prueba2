from django.http import HttpResponse;
from django.shortcuts import render, redirect, get_object_or_404;
from .models import *
from django.contrib.messages import constants as messages;
from django.contrib import messages;
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def inicio(request):
    instituciones=Institucion.objects.all()
    data = {'instituciones': instituciones}
    return render(request,"index.html",data)


def quienes_somos(request):
    print(request.user)
    return render(request, "quienes_somos.html")

def carreras(request):
    carreras = Carrera.objects.all()
    data = {'carrera': carreras}
    return render(request, "carreras.html", data)
def eliminarCarrera(request, IdCarrera):
    carrera = Carrera.objects.get(idcarrera=IdCarrera)
    carrera.delete()
    return redirect("carreras")
def editarCarrera(request, idcarrera):
    carrera = get_object_or_404(Carrera, idcarrera=idcarrera)

    if request.method == "POST":
        carrera.Nombre = request.POST['Nombre']
        carrera.Arancel = request.POST['Arancel']
        carrera.Duracion = request.POST['Duracion']
        carrera.idinstitucion.nombre = request.POST['institucion']
        carrera.idinstitucion.save()
        carrera.save()

        # Después de guardar, redireccionar a la lista o a donde desees
        return redirect('carreras')

    return render(request, 'editarC.html', {'carrera': carrera, 'instituciones': Institucion.objects.all()})

def instituciones(request):
    instituciones = Institucion.objects.all()
    data = {'instituciones': instituciones}
    return render(request, "instituciones.html", data)
def eliminarIntitucion(request, idinstitucion):
    institucion = Institucion.objects.get(idinstitucion=idinstitucion)
    institucion.delete()
    return redirect('instituciones')
def editarInstitucion(request, idinstitucion):
    institucion = get_object_or_404(Institucion, idinstitucion=idinstitucion)

    if request.method == 'POST':
        institucion.nombre = request.POST.get('nombre')
        institucion.region = request.POST.get('region')
        institucion.informacion = request.POST.get('informacion')
        institucion.url = request.POST.get('url')
        institucion.save()

        return redirect('instituciones')

    return render(request, 'editari.html', {'institucion': institucion})
def crearIntritucion(request):
    if request.method == "POST":
        nombre=request.POST['nombre']
        region=request.POST['region']
        informacion=request.POST['informacion']
        url=request.POST['url']

        registroI= Institucion()
        registroI.nombre=nombre
        registroI.region=region
        registroI.informacion=informacion
        registroI.url=url

        registroI.save()
    return render(request, "crearI.html")

def CrearCarrera(request):
    instituciones = Institucion.objects.all()
    data = {'instituciones': instituciones}

    if request.method == "POST":
        institucion_nombre = request.POST['institucion']
        nombre = request.POST['Nombre']
        arancel = request.POST['Arancel']
        duracion = request.POST['Duracion']

        # Asegúrate de que institucion_nombre esté definida aquí

        # Buscar la instancia de Institucion correspondiente al nombre seleccionado
        institucion = Institucion.objects.get(nombre=institucion_nombre)

        crearC = Carrera()
        crearC.idinstitucion = institucion  # Asignar la instancia de Institucion
        crearC.Nombre = nombre
        crearC.Arancel = arancel
        crearC.Duracion = duracion

        crearC.save()

    return render(request, "crearC.html", data)


def ingreso(request):
    return render(request,"ingreso_Instituciones.html")
    
def favorito(request):
    fav=Favorito.objects.all()
    data={'fav':fav}
    return render(request,"favorito.html",data)

def registroadministrador(request):
    if request.method == 'POST':
        Nombreadm = request.POST['Nombreadm']
        Apellidoadm = request.POST['Apellidoadm']
        correoadm = request.POST['correoadm']
        Contraseñaadm = request.POST['Contraseñaadm']

        try:
            if not (8 <= len(Contraseñaadm) <= 20):
                raise ValidationError('La contraseña debe tener entre 8 y 20 caracteres.')

            if not any(char.isupper() for char in Contraseñaadm) or not any(char.isdigit() for char in Contraseñaadm):
                raise ValidationError('La contraseña debe contener al menos una letra mayúscula y un número.')

            validate_password(Contraseñaadm)
        except ValidationError as e:
            messages.error(request, 'Contraseña no válida: {}'.format(', '.join(e.messages)))
            return render(request, "ingresousuarios/ingresoadministradores.html")

        hashed_password = make_password(Contraseñaadm)

        if administrador.objects.filter(correoadm=correoadm).exists():
            messages.error(request, 'El administrador con el correo electrónico {} ya está registrado.'.format(correoadm))
        else:
            administradorregister = administrador()
            administradorregister.Nombreadm = Nombreadm
            administradorregister.Apellidoadm = Apellidoadm
            administradorregister.correoadm = correoadm
            administradorregister.Contraseñaadm = hashed_password  
            administradorregister.save()
            messages.success(request, 'Administrador registrado con éxito, bienvenido {}'.format(Nombreadm))

    return render(request, "ingresousuarios/ingresoadministradores.html")

def registro(request):
    if request.method == "POST":
        Nombre = request.POST['Nombre']
        Apellido = request.POST['Apellido']
        correo = request.POST['correo']
        Contraseña = request.POST['Contraseña']

        try:
            if not (8 <= len(Contraseña) <= 20):
                raise ValidationError('La contraseña debe tener entre 8 y 20 caracteres.')

            if not any(char.isupper() for char in Contraseña) or not any(char.isdigit() for char in Contraseña):
                raise ValidationError('La contraseña debe contener al menos una letra mayúscula y un número.')

            validate_password(Contraseña)
        except ValidationError as e:
            messages.error(request, 'Contraseña no válida: {}'.format(', '.join(e.messages)))
            return render(request, "ingresousuarios/ingresousuarios.html")

        hashed_password = make_password(Contraseña)

        if Usuario.objects.filter(correo=correo).exists():
            messages.error(request, 'El usuario con el correo electrónico {} ya existe.'.format(correo))
        else:
            registro = Usuario()
            registro.Nombre = Nombre
            registro.Apellido = Apellido
            registro.correo = correo
            registro.Contraseña = hashed_password  
            registro.save()
            messages.success(request, 'Usuario registrado con éxito, bienvenido {}'.format(Nombre))
    
    return render(request, "ingresousuarios/ingresousuarios.html")


def loginusuarios(request):
    if request.method == "POST":
        correo = request.POST['email']
        contraseña = request.POST['password']

        try:
            detalleusuario = Usuario.objects.get(correo=correo)

            if check_password(contraseña, detalleusuario.Contraseña):
                request.session['correo'] = detalleusuario.Nombre
                return render(request, "index.html")
            else:
                messages.error(request, 'Correo o contraseña incorrectos')

        except Usuario.DoesNotExist:
            messages.error(request, 'Correo o contraseña incorrectos')
        
    return render(request, "login/login.html")

def loginadministrador(request):
    if request.method == "POST":
        email = request.POST['Email']
        Contraseñaadm = request.POST['password']

        try:
            detalleadm = administrador.objects.get(correoadm=email)

            if check_password(Contraseñaadm, detalleadm.Contraseñaadm):
                request.session['Email'] = detalleadm.Nombreadm
                return render(request, "index.html")
            else:
                print("Contraseña incorrecta para el administrador.")
                messages.error(request, 'Correo o contraseña incorrectos para el administrador  aaaaa')

        except administrador.DoesNotExist:
            print("No se encontró un administrador con este correo electrónico.")
            messages.error(request, 'Correo o contraseña incorrectos para el administrador')

    return render(request, "login/loginadm.html")
        


def cerrarsesionusuario(request):
    
    logout(request)

    return render(request,'index.html')

# def cerrarsesionusuario(request):
#     try:
#        del request.session['correo']
#     except :
#         return render(request,"index.html")
#     return render(request,"index.html")

def cerrarsesionadministrador(request):

    logout(request)

    return render(request, 'index.html')

def agregar_favorito(request):
    if request.method == 'POST':
        idcarrera = request.POST.get('idCarrera')
        idUsuario = request.session.get('id')

        if idUsuario is not None:
            usu = get_object_or_404(Usuario, idUsuario=idUsuario)
            carre = get_object_or_404(Carrera, idcarrera=idcarrera)

            # Verificar si ya existe el favorito para evitar duplicados
            favorito_existente = Favorito.objects.filter(idcarrera=carre, idUsuario=usu).exists()

            if not favorito_existente:
                agregarfav = Favorito(idcarrera=carre, idUsuario=usu)
                agregarfav.save()
                return redirect('carreras')
            else:
                # Puedes manejar aquí el caso de que ya exista el favorito
                messages.warning(request, 'Esta carrera ya está en tus favoritos.')
        else:
            # Puedes manejar aquí el caso de que no haya una sesión de usuario
            messages.error(request, 'Debes iniciar sesión para agregar favoritos.')

    return redirect('carreras')   




# def login(request):
#     if request.method == "POST":
#         #print(request.POST)
#         if ():
#             print("valido")

#             usuario = Usuario()

#             usuario.Nombre = usuario.cleaned_data['Nombre']
#             usuario.Apellido = usuario.cleaned_data['Apellido']
#             usuario.correo = usuario.cleaned_data['correo']
#             usuario.Contraseña = usuario.cleaned_data['Contraseña']

#             usuario.save()

#         else: 
#             print("invalido")


#     return render(request,"login.html")
