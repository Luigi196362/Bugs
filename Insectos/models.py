from django.db import models
from django.utils.timezone import now

class Insecto(models.Model):
    nombre = models.TextField(default='_',blank=False)
    nomcientifico = models.TextField(default='_',blank=False)
    clase = models.TextField(default='_',blank=False)
    orden = models.TextField(default='_',blank=False)
    familia = models.TextField(default='_',blank=False)
    habitat = models.TextField(default='_',blank=False)
    dieta = models.TextField(default='_',blank=False)
    longitud = models.TextField(default='_',blank=False)
    color = models.TextField(default='_',blank=False)
    numalas = models.TextField(default='_',blank=False)
    descripcion = models.TextField(default='_',blank=False)

# Create your models here.
