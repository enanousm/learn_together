from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.shortcuts import render
from . import controller as cont

def hola(request):
    return render(request, 'registro.html')

def registrar(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    contraseña = request.POST['contraseña']
    correo = request.POST['correo']
    rol = request.POST['rol']
    horarios = request.POST['horarios']
    if 'sexo' in request.POST:
        sexo = request.POST['sexo']
    else:
        sexo = None
    horario = None
    return HttpResponse()
