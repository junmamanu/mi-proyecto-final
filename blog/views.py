
from django.shortcuts import render
from blog.models import Configuracion
from blog.models import Usuarios
from django.views.generic import CreateView

def index(request):
    configuracion = Configuracion.objects.first()
    return render(request,"blog/index.html", {'configuracion': configuracion} )

class register(CreateView):
    model = Usuarios
    success_url = "/blog"
    fields = ["usuario","contraseña","nombre_apellido", "email","pais"]