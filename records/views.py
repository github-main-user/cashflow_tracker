from rest_framework import viewsets

from .models import CashFlowRecord
from .serializers import CashFlowRecordSerializer


class CashFlowRecordViewSet(viewsets.ModelViewSet):
    queryset = CashFlowRecord.objects.all()
    serializer_class = CashFlowRecordSerializer
