from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Categorie
from ..serializers import CategorieSerializer
from ..permissions import Admin, Editor, Viewer

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [IsAuthenticated, Admin, Editor, Viewer]