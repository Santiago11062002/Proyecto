from rest_framework import serializers
from .models import Libro

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ('id','referencia','nombre_autor','titulo_libro','fecha_publicacion','correo','descripcion','edad','ciudad','idioma','numero_paginas')
        read_only_fields = ('titulo_libro',)