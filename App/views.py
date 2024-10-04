from django.shortcuts import render, redirect

from .forms import *

from .models import *

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
