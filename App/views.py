from django.shortcuts import render, redirect

from .forms import *

from .models import *

def Home(request):
    return render(request, 'index.html')
