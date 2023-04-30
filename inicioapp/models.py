from django.db import models
from inicioapp.models import models
# Create your models here.
class cafe(models.Model):
    tipo = models.CharField(max_length=30)
    origen = models.CharField(max_length=30)
    especie = models.CharField(max_length=30)
    
class tipo_de_cafe(models.Model):
    ristreto = models.CharField(max_length=30)
    cafe_con_leche = models.CharField(max_length=30)
    americano = models.CharField(max_length=30)
    machiatto = models.CharField(max_length=30)
    capuccino = models.CharField(max_length=30)
    late = models.CharField(max_length=30)  
    cortado = models.CharField(max_length=30)
    
    class about_me(models.Model):
        nombre = models.CharField(max_length=30)
        apellido = models.CharField(max_length=30)
        edad = models.IntegerField(max_length=2)
        contacto = models.CharField(max_length=30)