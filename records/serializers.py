from rest_framework import serializers

from .models import CashFlowRecord


class CashFlowRecordSerializer(serializers.ModelSerializer):
    date = serializers.DateField(required=False)

    class Meta:
        model = CashFlowRecord
        fields = (
            "id",
            "date",
            "status",
            "flow_type",
            "category",
            "subcategory",
            "amount",
            "comment",
        )
