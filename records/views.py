from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .filters import CashFlowRecordFilter
from .models import CashFlowRecord
from .serializers import CashFlowRecordSerializer


class CashFlowRecordViewSet(viewsets.ModelViewSet):
    queryset = CashFlowRecord.objects.all()
    serializer_class = CashFlowRecordSerializer

    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    filterset_class = CashFlowRecordFilter
    search_fields = ("comment",)
    ordering_fields = ("date", "amount")
