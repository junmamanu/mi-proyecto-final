from ejemplo.models import Familiar
from ejemplo.models import Mascota
import datetime

Familiar(nombre="Rosario",fecha=datetime.date(1980, 10, 19), direccion="Av 9 de Julio 745", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", fecha=datetime.date(1997, 10, 19),direccion="Belgrano 152", numero_pasaporte=12341234).save()
Familiar(nombre="Samuel", fecha=datetime.date(2001, 10, 19),direccion="Salta 413", numero_pasaporte=12345123).save()
Familiar(nombre="Florencia", fecha=datetime.date(2022, 10, 19),direccion="San Martin 745", numero_pasaporte=12345612).save()

Mascota(nombre="Firulais", raza="Pastor Aleman", edad=5).save()
Mascota(nombre="Pelusa", raza="Persa", edad=3).save()
Mascota(nombre="Pirulais", raza="Pastor Aleman", edad=5).save()
Mascota(nombre="Pulusa", raza="Persa", edad=3).save()

print("Se cargo con exito los usuarios de pruebas")