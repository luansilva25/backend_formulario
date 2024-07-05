from ..models import Linguagens
from rest_framework.serializers import ModelSerializer

class LinguagemSerializers(ModelSerializer):
    class Meta:
        model = Linguagens
        fields = '__all__'