from rest_framework import serializers
from ..models import Editeur

class EditeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editeur
        fields = "__all__"
