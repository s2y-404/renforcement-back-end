from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Emprunt
from ..serializers import EmpruntSerializer
from ..permissions import Admin, Editor, Viewer

class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer
    permission_classes = [IsAuthenticated, Admin, Editor, Viewer]