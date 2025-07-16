from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import filters, viewsets

from .models import Category, FlowType, Status, SubCategory
from .serializers import (
    CategorySerializer,
    FlowTypeSerializer,
    StatusSerializer,
    SubCategorySerializer,
)


@extend_schema(tags=["Statuses"])
@extend_schema_view(
    list=extend_schema(
        summary="List all statuses",
        description="Retrieves a list of all statuses. Supports pagination, "
        "searching, filtering, and ordering.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a status",
        description="Retrieves the details of a specific status.",
    ),
    create=extend_schema(
        summary="Create a new status", description="Creates a new status."
    ),
    update=extend_schema(
        summary="Update a status", description="Updates an existing status."
    ),
    partial_update=extend_schema(
        summary="Partially update a status",
        description="Partially updates an existing status.",
    ),
    destroy=extend_schema(
        summary="Delete a status",
        description="Deletes a status. Can't delete a status in use.",
    ),
)
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    filter_backends = (filters.SearchFilter,)
    search_field = ("name",)


@extend_schema(tags=["Flow Types"])
@extend_schema_view(
    list=extend_schema(
        summary="List all flow types",
        description="Retrieves a list of all cash flow types. Supports pagination, "
        "searching, filtering, and ordering.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a flow type",
        description="Retrieves the details of a specific cash flow type.",
    ),
    create=extend_schema(
        summary="Create a new flow type", description="Creates a new cash flow type."
    ),
    update=extend_schema(
        summary="Update a flow type", description="Updates an existing cash flow type."
    ),
    partial_update=extend_schema(
        summary="Partially update a flow type",
        description="Partially updates an existing cash flow type.",
    ),
    destroy=extend_schema(
        summary="Delete a flow type",
        description="Deletes a cash flow type. Can't delete a flow type in use.",
    ),
)
class FlowTypeViewSet(viewsets.ModelViewSet):
    queryset = FlowType.objects.all()
    serializer_class = FlowTypeSerializer

    filter_backends = (filters.SearchFilter,)
    search_field = ("name",)


@extend_schema(tags=["Categories"])
@extend_schema_view(
    list=extend_schema(
        summary="List all categories",
        description="Retrieves a list of all categories. Supports pagination, "
        "searching, filtering, and ordering.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a category",
        description="Retrieves the details of a specific category.",
    ),
    create=extend_schema(
        summary="Create a new category", description="Creates a new category."
    ),
    update=extend_schema(
        summary="Update a category", description="Updates an existing category."
    ),
    partial_update=extend_schema(
        summary="Partially update a category",
        description="Partially updates an existing category.",
    ),
    destroy=extend_schema(
        summary="Delete a category",
        description="Deletes a category. Can't delete category in use.",
    ),
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("flow_type",)
    search_field = ("name",)


@extend_schema(tags=["Subcategories"])
@extend_schema_view(
    list=extend_schema(
        summary="List all subcategories",
        description="Retrieves a list of all subcategories. Supports pagination, "
        "searching, filtering, and ordering.",
    ),
    retrieve=extend_schema(
        summary="Retrieve a subcategory",
        description="Retrieves the details of a specific subcategory.",
    ),
    create=extend_schema(
        summary="Create a new subcategory", description="Creates a new subcategory."
    ),
    update=extend_schema(
        summary="Update a subcategory", description="Updates an existing subcategory."
    ),
    partial_update=extend_schema(
        summary="Partially update a subcategory",
        description="Partially updates an existing subcategory.",
    ),
    destroy=extend_schema(
        summary="Delete a subcategory",
        description="Deletes a subcategory. Can't delete category in use.",
    ),
)
class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("category",)
    search_field = ("name",)
