from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import controller as cont
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

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
    return render(request, 'registro.html')

def pagina_login(request):
    return render(request, 'login.html')

def loguear(request):
    try:
        correo = request.POST["correo"]
        contraseña = request.POST["contraseña"]
        user = authenticate(request, correo=correo, password=contraseña)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return redirect('login')
    except:
        return redirect('login')


def desloguear(request):
    logout(request)
    return loguear(request)


def registrar(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    contraseña = request.POST['contraseña']
    correo = request.POST['correo']
    rol = request.POST['rol']
    sexo = request.POST['sexo']
    horarios = organizar_horario(request)
    cont.insert_row(nombre,apellido,sexo,correo,contraseña,rol,horarios)
    return redirect('homepage')


@login_required
def pagina_homepage(request):
    return render(request, 'homepage.html')
