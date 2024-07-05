from ..models import Hobbies
from ..serializers import HobbiesSerializers
from rest_framework.viewsets import ModelViewSet

class HobbiesViewSet(ModelViewSet):
    queryset = Hobbies.objects.all()
    serializer_class = HobbiesSerializers