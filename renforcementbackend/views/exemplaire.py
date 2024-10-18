from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Exemplaire
from ..serializers import ExemplaireSerializer
from ..permissions import Admin, Editor, Viewer

class ExemplaireViewSet(viewsets.ModelViewSet):
    queryset = Exemplaire.objects.all()
    serializer_class = ExemplaireSerializer
    permission_classes = [IsAuthenticated, Admin, Editor, Viewer]