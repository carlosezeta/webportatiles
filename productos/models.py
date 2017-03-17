from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField
    fecha_pub = models.DateTimeField('fecha publicacion')