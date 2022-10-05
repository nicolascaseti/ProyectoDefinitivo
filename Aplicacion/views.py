from django.shortcuts import render
from Aplicacion.models import Familiar

from django.http import HttpResponse
from django.template import loader

# Create your views here.


def familiares(request):
    template = loader.get_template("familiares.html")
   
    familiar1 = Familiar(nombre="Pipo", apellido="Gorosito", edad="41", nac ="1995-01-05")
    familiar1.save()

    
    familiar2 = Familiar(nombre="Beto", apellido="Acosta", edad="36", nac ="1995-04-09")
    familiar2.save()
    
    familiar3 = Familiar(nombre="Pipi", apellido="Romanogli", edad="53", nac ="1995-06-25")
    familiar3.save()
    
    dic_de_contexto = {
        "familiar1" : familiar1,
        "familiar2" : familiar2,
        "familiar3" : familiar3,
    }
    
    response = template.render(dic_de_contexto)
    
    return HttpResponse(response)