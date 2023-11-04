from . import functions
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import userdata, ramo

###### RENDER PAGINAS ######
def pagina_registro(request):
    return render(request, 'registro.html', {'subtitulo':'Registrate ¡Es gratis!'})

def pagina_login(request):
    return render(request, 'login.html')

def pagina_homepage(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    else:
        username = request.user.username
        datos = (functions.buscar_usuario(username))[0]
        rol = datos[3]
        horario = datos[4]
        ramo = datos[5]
        lista_match = functions.match(ramo,horario,username)
        mhorarios = functions.recuperar_horario(horario)
        return render(request, 'homepage.html', {'horarios':mhorarios,'rol':rol,'ramo':ramo, 'match':lista_match})
    
def pagina_micuenta(request):
    if request.user.is_authenticated == False:
        return redirect('login')
    else:
        username = request.user.username
        datos = (functions.buscar_usuario(username))[0]
        rol = datos[3]
        horario = datos[4]
        ramo = datos[5]
        mhorarios = functions.recuperar_horario(horario)
        return render(request, 'micuenta.html',{'horarios':mhorarios,'rol':rol,'ramo':ramo})


############################################

###### FUNCIONES LOGIN Y LOGOUT ######
def loguear(request):
    try:
        username = request.POST["username"]
        password = request.POST["contraseña"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
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
        messages.error(request, 'El usuario ya esta ocupado')
        return redirect('registro')