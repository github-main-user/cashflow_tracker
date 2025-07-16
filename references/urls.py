from rest_framework.routers import DefaultRouter

from .apps import ReferencesConfig
from .views import CategoryViewSet, FlowTypeViewSet, StatusViewSet, SubCategoryViewSet

app_name = ReferencesConfig.name


status_router = DefaultRouter()
status_router.register("statuses", StatusViewSet, "status")

flow_type_router = DefaultRouter()
flow_type_router.register("flow-types", FlowTypeViewSet, "flow_type")

category_router = DefaultRouter()
category_router.register("categories", CategoryViewSet, "category")

subcategory_router = DefaultRouter()
subcategory_router.register("subcategories", SubCategoryViewSet, "subcategory")


urlpatterns = [
    *status_router.urls,
    *flow_type_router.urls,
    *category_router.urls,
    *subcategory_router.urls,
]
