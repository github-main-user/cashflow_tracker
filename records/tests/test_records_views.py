import pytest
from django.urls import reverse
from rest_framework import status

from records.models import CashFlowRecord
from references.models import Category, FlowType


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


# list


@pytest.mark.django_db
def test_list_records_empty_success(api_client):
    response = api_client.get(reverse("records:record-list"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("count") == 0


@pytest.mark.django_db
def test_list_records_success(api_client, record_obj):
    response = api_client.get(reverse("records:record-list"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("count") == 1


@pytest.mark.django_db
def test_list_records_filter_by_flow_type_success(api_client, record_obj):
    response = api_client.get(
        f"{reverse('records:record-list')}?flow_type={record_obj.flow_type.id}"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("count") == 1


@pytest.mark.django_db
def test_list_records_filter_by_wrong_flow_type_empty(api_client, record_obj):
    another_flow_type = FlowType.objects.create(name="another_flow_type")
    response = api_client.get(
        f"{reverse('records:record-list')}?flow_type={another_flow_type.id}"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("count") == 0


@pytest.mark.django_db
def test_list_records_filter_by_category_success(api_client, record_obj):
    response = api_client.get(
        f"{reverse('records:record-list')}?category={record_obj.category.id}"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("count") == 1


@pytest.mark.django_db
def test_list_records_filter_by_wrong_category_empty(
    api_client, record_obj, flow_type_obj
):
    another_category = Category.objects.create(
        name="another_category", flow_type=flow_type_obj
    )
    response = api_client.get(
        f"{reverse('records:record-list')}?category={another_category.id}"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("count") == 0


@pytest.mark.django_db
def test_list_records_search_by_comment_success(api_client, record_obj):
    response = api_client.get(
        f"{reverse('records:record-list')}?search={record_obj.comment}"
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("count") == 1


@pytest.mark.django_db
def test_list_records_search_by_wrong_comment_empty(api_client, record_obj):
    response = api_client.get(f"{reverse('records:record-list')}?search=WRONG")

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("count") == 0


@pytest.mark.django_db
def test_list_records_ordering_by_date_asc_success(api_client, record_obj):
    record_obj_2 = CashFlowRecord.objects.create(
        status=record_obj.status,
        flow_type=record_obj.flow_type,
        category=record_obj.category,
        subcategory=record_obj.subcategory,
        amount=15.2,
        comment="test comment",
    )
    response = api_client.get(f"{reverse('records:record-list')}?ordering=date")

    assert response.status_code == status.HTTP_200_OK
    results = response.data.get("results")
    assert len(results) == 2
    assert results[0].get("id") == record_obj.id
    assert results[1].get("id") == record_obj_2.id


@pytest.mark.django_db
def test_list_records_ordering_by_date_desc_success(api_client, record_obj):
    record_obj_2 = CashFlowRecord.objects.create(
        status=record_obj.status,
        flow_type=record_obj.flow_type,
        category=record_obj.category,
        subcategory=record_obj.subcategory,
        amount=15.2,
        comment="test comment",
    )
    response = api_client.get(f"{reverse('records:record-list')}?ordering=-date")

    assert response.status_code == status.HTTP_200_OK
    results = response.data.get("results")
    assert len(results) == 2
    assert results[0].get("id") == record_obj_2.id
    assert results[1].get("id") == record_obj.id


# create


@pytest.mark.django_db
def test_create_record_with_date_success(
    api_client, status_obj, flow_type_obj, category_obj, subcategory_obj
):
    response = api_client.post(
        reverse("records:record-list"),
        {
            "date": "2099-3-1",
            "status": status_obj.id,
            "flow_type": flow_type_obj.id,
            "category": category_obj.id,
            "subcategory": subcategory_obj.id,
            "amount": 25.35,
            "comment": "",
        },
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data
    assert CashFlowRecord.objects.filter(id=response.data.get("id")).exists()


@pytest.mark.django_db
def test_create_record_without_date_success(
    api_client, status_obj, flow_type_obj, category_obj, subcategory_obj
):
    response = api_client.post(
        reverse("records:record-list"),
        {
            "status": status_obj.id,
            "flow_type": flow_type_obj.id,
            "category": category_obj.id,
            "subcategory": subcategory_obj.id,
            "amount": 25.35,
            "comment": "",
        },
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data
    assert "date" in response.data
    assert CashFlowRecord.objects.filter(id=response.data.get("id")).exists()


@pytest.mark.django_db
def test_create_record_wrong_amount_fail(
    api_client, status_obj, flow_type_obj, category_obj, subcategory_obj
):
    response = api_client.post(
        reverse("records:record-list"),
        {
            "status": status_obj.id,
            "flow_type": flow_type_obj.id,
            "category": category_obj.id,
            "subcategory": subcategory_obj.id,
            "amount": -25.35,
            "comment": "",
        },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "id" not in response.data
    assert not CashFlowRecord.objects.filter(id=response.data.get("id")).exists()


@pytest.mark.django_db
def test_create_record_wrong_flow_type_fail(
    api_client, status_obj, category_obj, subcategory_obj
):

    response = api_client.post(
        reverse("records:record-list"),
        {
            "status": status_obj.id,
            "flow_type": FlowType.objects.create(name="anoter_flow_type").id,
            "category": category_obj.id,
            "subcategory": subcategory_obj.id,
            "amount": 25.35,
            "comment": "",
        },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "id" not in response.data
    assert not CashFlowRecord.objects.filter(id=response.data.get("id")).exists()


@pytest.mark.django_db
def test_create_record_wrong_category_fail(
    api_client, status_obj, flow_type_obj, subcategory_obj
):

    response = api_client.post(
        reverse("records:record-list"),
        {
            "status": status_obj.id,
            "flow_type": flow_type_obj.id,
            "category": Category.objects.create(
                name="new_category", flow_type=flow_type_obj
            ).id,
            "subcategory": subcategory_obj.id,
            "amount": 25.35,
            "comment": "",
        },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "id" not in response.data
    assert not CashFlowRecord.objects.filter(id=response.data.get("id")).exists()


# retrieve


@pytest.mark.django_db
def test_retrieve_record_success(api_client, record_obj):
    response = api_client.get(reverse("records:record-detail", args=[record_obj.id]))

    assert response.status_code == status.HTTP_200_OK
    assert "id" in response.data
    assert response.data.get("id") == record_obj.id


@pytest.mark.django_db
def test_retrieve_record_not_found_fail(api_client):
    response = api_client.get(reverse("records:record-detail", args=[0]))

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "id" not in response.data


# update


@pytest.mark.django_db
def test_update_record_success(api_client, record_obj):
    response = api_client.patch(
        reverse("records:record-detail", args=[record_obj.id]), {"amount": 999.9}
    )

    assert response.status_code == status.HTTP_200_OK
    assert "id" in response.data
    record_obj.refresh_from_db()
    assert float(record_obj.amount) == 999.9


@pytest.mark.django_db
def test_update_record_wrong_category_fail(api_client, flow_type_obj, record_obj):
    response = api_client.patch(
        reverse("records:record-detail", args=[record_obj.id]),
        {
            "category": Category.objects.create(
                name="NEW CATEGORY", flow_type=flow_type_obj
            ).id
        },
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "id" not in response.data
    record_obj.refresh_from_db()
    assert record_obj.category.name != "NEW CATEGORY"


# delete


@pytest.mark.django_db
def test_delete_record_success(api_client, record_obj):
    response = api_client.delete(reverse("records:record-detail", args=[record_obj.id]))

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not CashFlowRecord.objects.filter(id=record_obj.id).exists()
