from django.urls import path
 
from panel_mascota.views import MascotaList,MascotaCrear,MascotaBorrar


urlpatterns = [ 
    path('', MascotaList.as_view(), name="mascota-list"),
    path('mascota/crear', MascotaCrear.as_view(), name="mascota-crear"),
    path('mascota/<int:pk>/borrar', MascotaBorrar.as_view(), name= "mascota-borrar"),
    path('mascota/<int:pk>/actualizar', MascotaCrear.as_view(), name="mascota-actualizar"),
]