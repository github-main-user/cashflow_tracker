from django.utils import timezone
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

    def validate_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Date can't be in the future.")
        return value

    def validate(self, attrs):
        instance = self.instance

        # Retreive objects from instance when update, on create use provided data
        if instance:
            flow_type = attrs.get("flow_type", instance.flow_type)
            category = attrs.get("category", instance.category)
            subcategory = attrs.get("subcategory", instance.subcategory)
        else:
            flow_type = attrs.get("flow_type")
            category = attrs.get("category")
            subcategory = attrs.get("subcategory")

        if category and flow_type and category.flow_type != flow_type:
            raise serializers.ValidationError(
                {"category": "Category doesn't belong to given flow_type"}
            )

        if subcategory and category and subcategory.category != category:
            raise serializers.ValidationError(
                {"subcategory": "Subcategory doesn't belong to given category"}
            )

        return attrs
