from rest_framework.serializers import ModelSerializer
from ..models import Estados

class EstadosSerializers(ModelSerializer):
    class Meta:
        model = Estados
        fields = '__all__'