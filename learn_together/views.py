from django.http import HttpResponse
from django.shortcuts import render
from . import controller as cont

def hola(request):
    return render(request, 'registro.html')

def registrar(r):
    nombre = r.POST['nombre']
    apellido = r.POST['apellido']
    sexo = r.POST['sexo']
    correo = r.POST['correo']
    contraseña = r.POST['contraseña']
    rol = r.POST['rol']
    horario = r.POST['horario']
    
    mensaje = 'Estimado {}, sus datos han sido registrados satisfactoriamente'.format(nombre)
    return HttpResponse('Datos registrados')