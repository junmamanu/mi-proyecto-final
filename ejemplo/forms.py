from django import forms
from ejemplo.models import Familiar, Usuarios


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=10)

class FamiliarForm(forms.ModelForm):
    class Meta:
        model = Familiar
        fields = ['nombre', 'direccion', 'numero_pasaporte']


class AltaUsuario(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['usuario', 'contraseña', 'nombre_apellido']