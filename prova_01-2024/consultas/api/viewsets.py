from rest_framework import viewsets
from .serializers import ConsultaSerializer
from consultas.models import Consulta

class ConsultaViewSet(viewsets.ModelViewSet):
  queryset = Consulta.objects.all()
  serializer_class = ConsultaSerializer