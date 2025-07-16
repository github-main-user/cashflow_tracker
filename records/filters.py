import django_filters

from .models import CashFlowRecord


class CashFlowRecordFilter(django_filters.FilterSet):
    date_before = django_filters.DateFilter(field_name="date", lookup_expr="gte")
    date_after = django_filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = CashFlowRecord
        fields = ("status", "flow_type", "category", "subcategory")
