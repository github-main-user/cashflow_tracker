from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import filters, viewsets

from .filters import CashFlowRecordFilter
from .models import CashFlowRecord
from .serializers import CashFlowRecordSerializer


@extend_schema(tags=["Cash Flow Records"])
@extend_schema_view(
    list=extend_schema(
        summary="List all records",
        description="Retrieves a list of all cash flow records. Supports pagination, "
        "searching, filtering, and ordering.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a record",
        description="Retrieves the details of a specific cash flow record.",
    ),
    create=extend_schema(
        summary="Create a new record",
        description="Creates a new cash flow record.",
    ),
    update=extend_schema(
        summary="Update a record", description="Updates an existing cash flow record."
    ),
    partial_update=extend_schema(
        summary="Partially update a record",
        description="Partially updates an existing cash flow record.",
    ),
    destroy=extend_schema(
        summary="Delete a record", description="Deletes a cash flow record."
    ),
)
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
