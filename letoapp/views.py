from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from . import controller as cont
from .models import ramo, horario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import horario

def organizar_horario(request):
    horarios = ''
    hlu = request.POST.getlist(str('lu'))
    for h in hlu:
        horarios += h
    hma = request.POST.getlist(str('ma'))
    for h in hma:
        horarios += h
    hmi = request.POST.getlist(str('mi'))
    for h in hmi:
        horarios += h
    hju = request.POST.getlist(str('ju'))
    for h in hju:
        horarios += h
    hvi = request.POST.getlist(str('vi'))
    for h in hvi:
        horarios += h
    return horarios

def pagina_registro(request):
    return render(request, 'registro.html', {'subtitulo':'Registrate ¡Es gratis!'})

def pagina_login(request):
    return render(request, 'login.html')

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
        nuevo_horario = organizar_horario(request)
        user = User.objects.create_user(username=usuario,
                                        first_name=nombre,
                                        last_name=apellido,
                                        password=contraseña,
                                        email=correo
                                        )
        user.save()
        horario(username=usuario,
                n_horario=nuevo_horario,
                rol=rol).save()
        
        return redirect('login')
    except:
        messages.error(request, 'El usuario y/o contraseña ya estan ocupados')
        return redirect('registro')


@login_required
def pagina_homepage(request):
    return render(request, 'homepage.html')
