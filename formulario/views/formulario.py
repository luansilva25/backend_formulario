from ..models import Formulario
from ..serializers import FormularioCreateSerializer, FormularioReadSerializer
from rest_framework.viewsets import ModelViewSet

class FormularioViewSet(ModelViewSet):
    queryset = Formulario.objects.all()
    def get_serializer_class(self):
        print(self.action)
        if self.action == 'create' or self.action == 'update':
            return FormularioCreateSerializer
        return FormularioReadSerializer