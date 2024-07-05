from ..models import Linguagens
from ..serializers import LinguagemSerializers
from rest_framework.viewsets import ModelViewSet

class LinguagensViewSet(ModelViewSet):
    queryset =Linguagens.objects.all()
    serializer_class = LinguagemSerializers