from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.shortcuts import render
from . import controller as cont


def hola(request):
    return render(request, 'registro.html')

def registrar(request):
    
    return HttpResponse('hola')