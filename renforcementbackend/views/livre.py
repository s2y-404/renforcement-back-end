from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Livre
from ..serializers import LivreSerializer
from ..filters import LivrePagination

class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    pagination_class = LivrePagination

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['auteurs__nom', 'categories__nom']
    ordering_fields = ['titre', 'date_de_publication']
    ordering = ['titre']