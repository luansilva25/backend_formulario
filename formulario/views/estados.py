from ..serializers import EstadosSerializers
from ..models import Estados
from rest_framework.viewsets import ModelViewSet

class EstadoViewSet(ModelViewSet):
    queryset = Estados.objects.all()
    serializer_class = EstadosSerializers