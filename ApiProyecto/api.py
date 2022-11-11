from .models import Libro
from rest_framework import viewsets, permissions
from .serializers import ProyectoSerializer

class ProyectoviewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProyectoSerializer