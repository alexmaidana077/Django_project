from django import forms
from .models import *

class Nuevo_Remedio(forms.ModelForm):
    class Meta:
        model=Remedios
        fields='__all__'

class Nueva_Receta(forms.ModelForm):
    class Meta:
        model=SubirReceta
        fields='__all__'

