import pytest
from django.core.exceptions import ValidationError

from records.models import CashFlowRecord
from references.models import Category, FlowType


def test_wrong_flow_type_type_clean_fail(record_obj):
    with pytest.raises(ValidationError):
        record = CashFlowRecord(
            status=record_obj.status,
            flow_type=FlowType.objects.create(name="new type"),
            category=record_obj.category,
            subcategory=record_obj.subcategory,
            amount=15.2,
            comment="test comment",
        )
        record.full_clean()


def test_wrong_category_clean_fail(record_obj):
    with pytest.raises(ValidationError):
        record = CashFlowRecord(
            status=record_obj.status,
            flow_type=record_obj.flow_type,
            category=Category.objects.create(
                name="name", flow_type=record_obj.flow_type
            ),
            subcategory=record_obj.subcategory,
            amount=15.2,
            comment="test comment",
        )
        record.full_clean()


def test_date_in_future_clean_fail(record_obj):
    with pytest.raises(ValidationError):
        record = CashFlowRecord(
            date="2099-1-1",
            status=record_obj.status,
            flow_type=record_obj.flow_type,
            category=record_obj.category,
            subcategory=record_obj.subcategory,
            amount=15.2,
            comment="test comment",
        )
        record.full_clean()
