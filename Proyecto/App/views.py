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

@login_required
@permission_required('App.add_remedios')
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

@permission_required('App.change_remedios')
def Modificar_Remedios(request,Codigo):
    sql=get_object_or_404(Remedios,Codigo=Codigo)
    data={
        'forms':Nuevo_Remedio(instance=sql)
    }
    if request.method=='POST':
        query=Nuevo_Remedio(data=request.POST,instance=sql,files=request.FILES)
        if  query.is_valid():
            query.save()
            data['mensaje']="Datos Modificados Correctamente "
        else:
            data['forms']=Nuevo_Remedio
    return render (request,'Pages/modificar.html',data)

# boton eliminar
@permission_required('App.delete_remedios')
def Eliminar_Remedios(request,Codigo):
    buscar=get_object_or_404(Remedios,Codigo=Codigo)
    buscar.delete()
    return redirect(to="home")

def Ver_Producto(request):
    forms = Remedios.objects.all()
    data = {
        'forms': forms
    }
    return render (request, 'Pages/vistas.html', data)

def Agregar_Receta(request):
    data = {
        'forms': Nueva_Receta()
    }
    if request.method == 'POST':
        query = Nueva_Receta(request.POST, request.FILES)
        if query.is_valid():
            query.save()
            data['manin'] = "Registrado Correctamente"
        else:
            data['forms'] = query 
    return render(request, 'Pages/agregar.html', data)

def Salir(request):
    logout(request)
    return redirect(to='home')


