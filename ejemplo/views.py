from django.shortcuts import render
from ejemplo.models import Familiar, Mascota
from ejemplo.forms import Buscar, FamiliarForm, AltaUsuario, AltaMascota, buscarMascota
from django.views import View 

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

def mostrar_mascota(request):
    lista_mascotas = Mascota.objects.all()
    return render(request, "ejemplo/mascotas.html", {"lista_mascotas": lista_mascotas})

class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})


class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})



class AltaUsuario(View):

    form_class = AltaUsuario
    template_name = 'ejemplo/alta_nuevo_usuario.html'
    initial = {"usuario":"", "contraseña":"", "nombre_apellido":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito un usuario con exito{form.cleaned_data.get('usuario')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})



class AltaMascota(View):

    form_class = AltaMascota
    template_name = 'ejemplo/alta_mascota.html'
    initial = {"nombre":"", "raza":"", "edad":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito una mascota con exito{form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class BuscarMascota(View):

    form_class = buscarMascota
    template_name = 'ejemplo/buscar_mascota.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_mascotas = Mascota.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_mascotas':lista_mascotas})

        return render(request, self.template_name, {"form": form})