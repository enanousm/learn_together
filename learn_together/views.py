from django.http import HttpResponse
from django.shortcuts import render
from . import controller as cont

def hola(request):
    return render(request, 'registro.html')

def registrar(r):
    nombre = r.GET['nombre']
    apellido = r.GET['apellido']
    sexo = r.GET['sexo']
    correo = r.GET['correo']
    contraseña = r.GET['contraseña']
    rol = r.GET['rol']
    horario = r.GET['horario']
    
    mensaje = 'Estimado {}, sus datos han sido registrados satisfactoriamente'.format(nombre)
    return HttpResponse('Datos registrados')