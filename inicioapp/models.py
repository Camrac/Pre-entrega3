from django.db import models

# Create your models here.
class cafe(models.Model):
    tipo: models.CharField(max_length=30)
    origen=models.CharField(max_length=30)
    especie=models.CharField(max_length=30)
