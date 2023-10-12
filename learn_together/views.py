from django.http import HttpResponse
from django.template import Template, Context

def hola(request):
    plantillaExt = open("templates/registro.html")
    template = Template(plantillaExt.read())
    plantillaExt.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)
