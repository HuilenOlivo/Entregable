from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse


# Create your views here.

def familiares(request):
    padre= Familiar(parentesco="Padre", nombre="Gabriel", edad=56, nacimiento="1962-02-26")
    padre.save()

    madre = Familiar( parentesco="Madre", nombre="Susana", edad=46, nacimiento="1996-11-01") 
    madre.save()

    hermano = Familiar(parentesco="Hermano", nombre="Agustin", edad=29, nacimiento="1991-12-09") 
    hermano.save()

    listaFamiliares =[padre, madre, hermano]

    return render(request, 'AppClase/familiares.html', {'familiares':listaFamiliares})