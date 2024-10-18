from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Auteur
from ..serializers import AuteurSerializer
from ..permissions import Admin, Editor, Viewer

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
    permission_classes = [IsAuthenticated, Admin, Editor, Viewer]