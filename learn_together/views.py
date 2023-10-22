from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.shortcuts import render
from . import controller as cont

def registro(request):
    return render(request, 'registro.html')

def asignar_horarios(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    contraseña = request.POST['contraseña']
    correo = request.POST['correo']
    rol = request.POST['rol']
    horarios = None
    if 'sexo' in request.POST:
        sexo = request.POST['sexo']
    else:
        sexo = None
    #cont.insert_row(nombre,apellido,sexo,correo,contraseña,rol,horarios)
    return render(request, 'asignar_horarios.html')
