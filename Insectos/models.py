from django.db import models
from django.utils.timezone import now
from django.conf import settings
# ...code

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

posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    insecto = models.ForeignKey('Insectos.Insecto', related_name='insectos', on_delete=models.CASCADE)
# Create your models here.
