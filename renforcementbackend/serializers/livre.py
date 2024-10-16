from rest_framework import serializers
from ..models import Livre

class LivreSerializer(serializers.ModelSerializer):
    auteurs = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)
    editeur = serializers.StringRelatedField() 

    class Meta:
        model = Livre
        fields = "__all__"
