from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import controller as cont
from django.contrib.auth.decorators import login_required

def registro(request):
    return render(request, 'registro.html')

def registrado(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    contraseña = request.POST['contraseña']
    correo = request.POST['correo']
    rol = request.POST['rol']
    if 'sexo' in request.POST:
        sexo = request.POST['sexo']
    else:
        sexo = None
    horarios = request.POST.getlist('lu')
    #cont.insert_row(nombre,apellido,sexo,correo,contraseña,rol,horarios)
    return HttpResponse(horarios)

@login_required
def registrar_horario(request):
    mensaje= request.POST
    return 0
