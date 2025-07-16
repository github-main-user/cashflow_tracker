from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Category, FlowType, Status, SubCategory
from .serializers import StatusSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    filter_backends = (filters.SearchFilter,)
    search_field = ("name",)


class FlowTypeViewSet(viewsets.ModelViewSet):
    queryset = FlowType.objects.all()
    serializer_class = StatusSerializer

    filter_backends = (filters.SearchFilter,)
    search_field = ("name",)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = StatusSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("flow_type",)
    search_field = ("name",)


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = StatusSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("category",)
    search_field = ("name",)
