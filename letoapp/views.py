from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from . import controller as cont
from .models import ramo, horario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import userdata

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

def pagina_homepage(request):
    if request.user.is_authenticated:
        username = request.user.username
        datos = (cont.search_user(username))[0]
        rol = datos[3]
        horarios = datos[4]
        ramo = datos[5]
        mhorarios = cont.recuperar_horario(horarios)
        return render(request, 'homepage.html', {'horarios':mhorarios,'rol':rol,'ramo':ramo})
        return HttpResponse(datos)
    else:
        return redirect('login')
    
def pagina_micuenta(request):
    if request.user.is_authenticated:
        return render(request, 'micuenta.html')
    else:
        return redirect('login')