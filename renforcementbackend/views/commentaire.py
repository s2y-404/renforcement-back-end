from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets
from ..models import Commentaire
from ..serializers import CommentaireSerializer
from ..filters import CommentairePagination

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    pagination_class = CommentairePagination

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['note', 'visible', 'modéré', 'livre__titre']
    ordering_fields = ['note', 'date_publication']
    ordering = ['date_publication']