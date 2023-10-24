from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import controller as cont
from django.contrib.auth.decorators import login_required

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

def inicio(request):
    return render(request, 'registro.html')

def registrar(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    contraseña = request.POST['contraseña']
    correo = request.POST['correo']
    rol = request.POST['rol']
    sexo = request.POST['sexo']
    horarios = organizar_horario(request)
    cont.insert_row(nombre,apellido,sexo,correo,contraseña,rol,horarios)
    return homepage(request)


@login_required
def homepage(request):
    return render(request, 'homepage.html')
