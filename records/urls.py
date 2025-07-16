from rest_framework.routers import DefaultRouter

from .apps import RecordsConfig
from .views import CashFlowRecordViewSet

app_name = RecordsConfig.name


records_router = DefaultRouter()
records_router.register("", CashFlowRecordViewSet, "record")

urlpatterns = records_router.urls
