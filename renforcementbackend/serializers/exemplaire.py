from rest_framework import serializers
from ..models import Exemplaire

class ExemplaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exemplaire
        fields = "__all__"
