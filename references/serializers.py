from rest_framework import serializers

from .models import Category, FlowType, Status, SubCategory


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ("id", "name")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "flow_type")


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ("id", "name", "category")


class FlowTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlowType
        fields = ("id", "name")
