from django.utils import timezone
from rest_framework import serializers

from references.services import ensure_category_consistency

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

    def validate_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Date can't be in the future.")
        return value

    def validate(self, attrs):
        instance = self.instance

        # Retreive object from instance when it is, otherwise use provided data
        if instance:
            flow_type = attrs.get("flow_type", instance.flow_type)
            category = attrs.get("category", instance.category)
            subcategory = attrs.get("subcategory", instance.subcategory)
        else:
            flow_type = attrs.get("flow_type")
            category = attrs.get("category")
            subcategory = attrs.get("subcategory")

        ensure_category_consistency(flow_type, category, subcategory)

        return attrs
