from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Commentaire
from ..serializers import CommentaireSerializer
from ..filters import CommentairePagination
from ..permissions import Admin, Editor, Viewer

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    pagination_class = CommentairePagination
    permission_classes = [IsAuthenticated, Admin, Editor, Viewer]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['note', 'visible', 'modéré', 'livre__titre']
    ordering_fields = ['note', 'date_publication']
    ordering = ['date_publication']