from django.shortcuts import render,get_object_or_404,redirect
#---->Importamos el Sector de Formularios
from .forms import *
from .models import *
#--->Importamos la Libreria de Logout
from django.contrib.auth import logout
#--->Importamos la Libreria de Permisos
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

def Home(request):
    return render(request, 'index.html')

def Agregar(request):
    data = {
        'forms': Nuevo_Remedio()
    }
    if request.method == 'POST':
        query = Nuevo_Remedio(request.POST, request.FILES)
        if query.is_valid():
            query.save()
            data['manin'] = "Registrado Correctamente"
        else:
            data['forms'] = query 
    return render(request, 'Pages/agregar.html', data)


def Ver_Producto(request):
    forms = Remedios.objects.all()
    data = {
        'forms': forms
    }
    return render (request, 'Pages/vistas.html', data)

def Salir(request):
    logout(request)
    return redirect(to='home')


