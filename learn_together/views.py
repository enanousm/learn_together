<from django.http import HttpResponse
from django.template import Template, Context

def hola(request):
    plantillaExt = open("C:\Users\enano\Documents\Enano\Int a la Ingenieria 2023\learn_together\learn_together\templates\plantilla_hola.html")
    template = Template(plantillaExt.read())
    plantillaExt.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)
