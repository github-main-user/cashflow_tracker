import pytest
from rest_framework.test import APIClient

from records.models import CashFlowRecord
from references.models import Category, FlowType, Status, SubCategory


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def status_obj(db) -> Status:
    return Status.objects.create(name="test_status")


@pytest.fixture
def flow_type_obj(db) -> FlowType:
    return FlowType.objects.create(name="test_flow_type")


@pytest.fixture
def category_obj(db, flow_type_obj) -> Category:
    return Category.objects.create(name="test_category", flow_type=flow_type_obj)


@pytest.fixture
def subcategory_obj(db, category_obj) -> Category:
    return SubCategory.objects.create(name="test_category", category=category_obj)


@pytest.fixture
def record_obj(
    db, status_obj, flow_type_obj, category_obj, subcategory_obj
) -> CashFlowRecord:
    return CashFlowRecord.objects.create(
        status=status_obj,
        flow_type=flow_type_obj,
        category=category_obj,
        subcategory=subcategory_obj,
        amount=15.2,
        comment="test comment",
    )
