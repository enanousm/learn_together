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

def registro(request):
    return render(request, 'registro.html')

def registrado(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    contraseña = request.POST['contraseña']
    correo = request.POST['correo']
    rol = request.POST['rol']
    sexo = request.POST['sexo']
    horarios = organizar_horario(request)
    cont.insert_row(nombre,apellido,sexo,correo,contraseña,rol,horarios)
    return HttpResponse('Datos registrados')

@login_required
def registrar_horario(request):
    mensaje= request.POST
    return 0
