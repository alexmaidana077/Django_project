from django.db import models

# Create your models here.
class Remedios(models.Model):
    Codigo=models.AutoField(primary_key=True)
    Nombre=models.TextField(max_length=30)
    Descripcion=models.TextField(max_length=150)
    Precio = models.FloatField()
    Imagen=models.ImageField(upload_to="Remedios",null=True)

    def __int__(self):
        self.Codigo