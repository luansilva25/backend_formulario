from rest_framework.serializers import ModelSerializer
from ..models import Formulario

class FormularioCreateSerializer(ModelSerializer):
    class Meta:
        model = Formulario
        fields = '__all__'

class FormularioReadSerializer(ModelSerializer):
    class Meta:
        model = Formulario
        fields = '__all__'
        depth = 2