from rest_framework import serializers
from ..models import Auteur

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = "__all__"
