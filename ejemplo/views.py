from django.shortcuts import render
from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    suma = 12+12
    return render(request, "ejemplo/saludar.html", {
        "nombre":"german",
        "nombre" :suma        
        
        
        })


def index_dos(request, nombre , apellido):
    return render(request, "ejemplo/saludar.html", {
        "nombre": nombre ,
        "apellido" :apellido      
        
        
        })

def index_tres(request):

    return render (request, "ejemplo/saludar.html",{
        
        "notas": [1,2,3,4,4,5,6,7,8]

    })

def imc(request, peso, altura):
    altura_en_metros = altura/100
    peso_en_kilos = peso
    imccalculo = (altura_en_metros/peso_en_kilos)
    imc = imccalculo
    return render (request, "ejemplo/imc.html",)


def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})