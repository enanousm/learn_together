from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import userdata
from django.conf import settings
from django.core.mail import send_mail

from . import functions

###### RENDER PAGINAS ######
def pagina_registro(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    return render(request, 'registro.html')

def pagina_login(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    return render(request, 'login.html')

def pagina_homepage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        username = request.user.username
        datos = (functions.buscar_usuario(username))[0]
        rol = datos[3]
        horario = datos[4]
        ramo = datos[5]
        if ramo == 'none123':
            ramo = None
        elif ramo == 'new_123':
            ramo = 0
        lista_match = functions.match(ramo,horario,username)
        mhorarios = functions.recuperar_horario(horario)
        return render(request, 'homepage.html', {'horarios':mhorarios,'rol':rol,'ramo':ramo, 'match':lista_match})
    
def pagina_micuenta(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        username = request.user.username
        datos = (functions.buscar_usuario(username))[0]
        rol = datos[3]
        horario = datos[4]
        ramo = datos[5]
        mhorarios = functions.recuperar_horario(horario)
        return render(request, 'micuenta.html',{'horarios':mhorarios,'rol':rol,'ramo':ramo})

def pagina_horario(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, 'horarios.html')

############################################

###### FUNCIONES LOGIN, LOGOUT Y RAMO ######
def loguear(request):
    try:
        username = request.POST["username"]
        password = request.POST["contraseña"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            mensaje = f'Usuario y/o contraseña invalidos'
            messages.warning(request, mensaje)
            return redirect('login')
    except:
        return redirect('login')
    
def desloguear(request):
    logout(request)
    return redirect('login')

def registrar(request):
    try:
        usuario = request.POST['username']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        contraseña = request.POST['contraseña']
        correo = request.POST['correo']
        rol = request.POST['rol']
        nuevo_horario = functions.organizar_horario(request)
        User.objects.create_user(username=usuario,
                                first_name=nombre,
                                last_name=apellido,
                                password=contraseña,
                                email=correo).save()
        userdata(username=usuario,
                n_horario=nuevo_horario,
                rol=rol,
                first_name=nombre,
                last_name=apellido,
                email=correo,
                ).save()
        
        return redirect('login')
    except:
        messages.error(request, 'El usuario no se encuentra disponible')
        return redirect('registro')

def ramo(request):
    username = request.user.username
    ramo = request.POST["selecc_ramo"]
    ramo = functions.ramo(ramo)
    functions.insertar_ramo(username,ramo)
    return redirect ('homepage')

def email(request,correo):
    send_mail(
    '¡Nuevo MATCH en Learn together!',
    f'{request.user.first_name} {request.user.last_name} ha coincidido contigo.\n¡Contactense!\n{request.user.email}',
    settings.EMAIL_HOST_USER,
    [correo],
    fail_silently=False
    )
    mensaje = f'¡Correo enviado a {correo} satisfactoriamente!'
    messages.success(request, mensaje)
    return redirect ('homepage')

def actualizar(request):
    nuevo_horario = functions.organizar_horario(request)
    username = request.user.username
    functions.actualizar_horario(username,nuevo_horario)
    mensaje = f'¡Horario actualizado correctamente!'
    messages.success(request, mensaje)
    return redirect('homepage')