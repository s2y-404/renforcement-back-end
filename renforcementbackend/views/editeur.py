from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Editeur
from ..serializers import EditeurSerializer
from ..permissions import Admin, Editor, Viewer

class EditeurViewSet(viewsets.ModelViewSet):
    queryset = Editeur.objects.all()
    serializer_class = EditeurSerializer
    permission_classes = [IsAuthenticated, Admin, Editor, Viewer]