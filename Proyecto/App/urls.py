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
    path('logouts/',Salir,name='logouts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
