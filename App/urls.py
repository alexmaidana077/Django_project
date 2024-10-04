from django.urls import path
#-->Importamos las Vistas para las URL
from .views import *

urlpatterns =[
    path('agregar/',Agregar,name='agregar'),
    path('vistas/', Ver_Producto,name= 'vistas'),
]