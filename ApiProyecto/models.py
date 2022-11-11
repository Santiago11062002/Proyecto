from django.db import models

# Create your models here.

class Libro(models.Model):
    referencia = models.CharField(max_length=200)
    nombre_autor = models.CharField(max_length=200)
    titulo_libro = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    correo = models.EmailField(blank=True)
    descripcion = models.TextField()
    edad = models.PositiveIntegerField(default=0)
    ciudad = models.CharField(max_length=200)
    idioma = models.CharField(max_length=200)
    numero_paginas = models.PositiveIntegerField(default=0)





