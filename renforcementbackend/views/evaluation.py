from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Evaluation
from ..serializers import EvaluationSerializer
from ..permissions import Admin, Editor, Viewer

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    permission_classes = [IsAuthenticated, Admin, Editor, Viewer]