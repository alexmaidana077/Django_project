from django.contrib import admin
from django.urls import path
#---->Importamos Settings
from django.conf import settings
#----> Importar Static
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', Home, name='home'),  
    path('agregar/',Agregar,name='agregar'),
    path('vistas/', Ver_Producto,name= 'vistas'),
    path('modificar/<Codigo>/',Modificar_Remedios,name='modificar'),
    path('eliminar/<Codigo>/',Eliminar_Remedios,name='eliminar'),
    path('logouts/',Salir,name='logouts'),
]

