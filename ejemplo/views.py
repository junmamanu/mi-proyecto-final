from django.shortcuts import render


def index(request):
    suma = 12+12
    return render(request, "ejemplo/saludar.html", {
        "nombr":"german",
        "nombre" :suma        
        
        
        })


def index_dos(request, nombre , apellido):
    return render(request, "ejemplo/saludar.html", {
        "nombr":nombre ,
        "nombre" :apellido        
        
        
        })

def index_tres(request):

    return render (request, "ejemplo/saludar.html",{
        
        "notas": [1,2,3,4,4,5,6,7,8]
    

    
    
    })

def imc(request, peso, altura):
    peso = peso
    altura
    return render (request, "ejemplo/imc.html",{"imc":imc})

