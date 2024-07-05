from rest_framework.serializers import ModelSerializer
from ..models import Hobbies

class HobbiesSerializers(ModelSerializer):
    class Meta:
        model = Hobbies
        fields = '__all__'