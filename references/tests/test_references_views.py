import pytest
from django.db.models.deletion import ProtectedError
from django.urls import reverse
from rest_framework import status

from references.models import Category, FlowType, Status, SubCategory

# ========
#  status
# ========

# list


@pytest.mark.django_db
def test_status_list(api_client, status_obj):
    response = api_client.get(reverse("references:status-list"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("count") == Status.objects.count()
    assert "results" in response.data


# create


@pytest.mark.django_db
def test_status_create_success(api_client):
    response = api_client.post(
        reverse("references:status-list"), {"name": "new_status"}
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data
    assert Status.objects.filter(id=response.data.get("id")).exists()


@pytest.mark.django_db
def test_status_create_already_exists_fail(api_client, status_obj):
    response = api_client.post(
        reverse("references:status-list"), {"name": status_obj.name}
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "id" not in response.data
    assert Status.objects.filter(id=status_obj.id).count() == 1


# retrieve


@pytest.mark.django_db
def test_status_retrieve_success(api_client, status_obj):
    response = api_client.get(reverse("references:status-detail", args=[status_obj.id]))

    assert response.status_code == status.HTTP_200_OK
    assert "id" in response.data


@pytest.mark.django_db
def test_status_retrieve_not_found_fail(api_client):
    response = api_client.get(reverse("references:status-detail", args=[0]))

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "id" not in response.data


# update


@pytest.mark.django_db
def test_status_update_success(api_client, status_obj):
    response = api_client.patch(
        reverse("references:status-detail", args=[status_obj.id]), {"name": "UPDATED"}
    )

    assert response.status_code == status.HTTP_200_OK
    assert "id" in response.data
    status_obj.refresh_from_db()
    assert status_obj.name == "UPDATED"


# delete


@pytest.mark.django_db
def test_status_delete_success(api_client, status_obj):
    response = api_client.delete(
        reverse("references:status-detail", args=[status_obj.id])
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Status.objects.filter(id=status_obj.id).exists()


@pytest.mark.django_db
def test_status_delete_in_use_fail(api_client, status_obj, record_obj):
    with pytest.raises(ProtectedError):
        api_client.delete(reverse("references:status-detail", args=[status_obj.id]))

    assert Status.objects.filter(id=status_obj.id).exists()


# ===========
#  flow_type
# ===========

# list


@pytest.mark.django_db
def test_flow_type_list(api_client, flow_type_obj):
    response = api_client.get(reverse("references:flow_type-list"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("count") == FlowType.objects.count()
    assert "results" in response.data


# create


@pytest.mark.django_db
def test_flow_type_create_success(api_client):
    response = api_client.post(
        reverse("references:flow_type-list"), {"name": "new_flow_type"}
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data
    assert FlowType.objects.filter(id=response.data.get("id")).exists()


@pytest.mark.django_db
def test_flow_type_create_already_exists_fail(api_client, flow_type_obj):
    response = api_client.post(
        reverse("references:flow_type-list"), {"name": flow_type_obj.name}
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "id" not in response.data
    assert FlowType.objects.filter(id=flow_type_obj.id).count() == 1


# retrieve


@pytest.mark.django_db
def test_flow_type_retrieve_success(api_client, flow_type_obj):
    response = api_client.get(
        reverse("references:flow_type-detail", args=[flow_type_obj.id])
    )

    assert response.status_code == status.HTTP_200_OK
    assert "id" in response.data


@pytest.mark.django_db
def test_flow_type_retrieve_not_found_fail(api_client):
    response = api_client.get(reverse("references:flow_type-detail", args=[0]))

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "id" not in response.data


# update


@pytest.mark.django_db
def test_flow_type_update_success(api_client, flow_type_obj):
    response = api_client.patch(
        reverse("references:flow_type-detail", args=[flow_type_obj.id]),
        {"name": "UPDATED"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert "id" in response.data
    flow_type_obj.refresh_from_db()
    assert flow_type_obj.name == "UPDATED"


# delete


@pytest.mark.django_db
def test_flow_type_delete_success(api_client, flow_type_obj):
    response = api_client.delete(
        reverse("references:flow_type-detail", args=[flow_type_obj.id])
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not FlowType.objects.filter(id=flow_type_obj.id).exists()


@pytest.mark.django_db
def test_flow_type_delete_in_use_fail(api_client, flow_type_obj, record_obj):
    with pytest.raises(ProtectedError):
        api_client.delete(
            reverse("references:flow_type-detail", args=[flow_type_obj.id])
        )

    assert FlowType.objects.filter(id=flow_type_obj.id).exists()


# ==========
#  category
# ==========

# list


@pytest.mark.django_db
def test_category_list(api_client, category_obj):
    response = api_client.get(reverse("references:category-list"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("count") == Category.objects.count()
    assert "results" in response.data


# create


@pytest.mark.django_db
def test_category_create_success(api_client, flow_type_obj):
    response = api_client.post(
        reverse("references:category-list"),
        {"name": "new_category", "flow_type": flow_type_obj.id},
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data
    assert Category.objects.filter(id=response.data.get("id")).exists()


@pytest.mark.django_db
def test_category_create_already_exists_for_flow_type_fail(api_client, category_obj):
    response = api_client.post(
        reverse("references:category-list"),
        {"name": category_obj.name, "flow_type": category_obj.flow_type.id},
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "id" not in response.data
    assert Category.objects.filter(id=category_obj.id).count() == 1


# retrieve


@pytest.mark.django_db
def test_category_retrieve_success(api_client, category_obj):
    response = api_client.get(
        reverse("references:category-detail", args=[category_obj.id])
    )

    assert response.status_code == status.HTTP_200_OK
    assert "id" in response.data


@pytest.mark.django_db
def test_category_retrieve_not_found_fail(api_client):
    response = api_client.get(reverse("references:category-detail", args=[0]))

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "id" not in response.data


# update


@pytest.mark.django_db
def test_category_update_success(api_client, category_obj):
    response = api_client.patch(
        reverse("references:category-detail", args=[category_obj.id]),
        {"name": "UPDATED"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert "id" in response.data
    category_obj.refresh_from_db()
    assert category_obj.name == "UPDATED"


# delete


@pytest.mark.django_db
def test_category_delete_success(api_client, category_obj):
    response = api_client.delete(
        reverse("references:category-detail", args=[category_obj.id])
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Category.objects.filter(id=category_obj.id).exists()


@pytest.mark.django_db
def test_category_delete_in_use_fail(api_client, category_obj, record_obj):
    with pytest.raises(ProtectedError):
        api_client.delete(reverse("references:category-detail", args=[category_obj.id]))

    assert Category.objects.filter(id=category_obj.id).exists()


# =============
#  subcategory
# =============

# list


@pytest.mark.django_db
def test_subcategory_list(api_client, subcategory_obj):
    response = api_client.get(reverse("references:subcategory-list"))

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("count") == SubCategory.objects.count()
    assert "results" in response.data


# create


@pytest.mark.django_db
def test_subcategory_create_success(api_client, category_obj):
    response = api_client.post(
        reverse("references:subcategory-list"),
        {"name": "new_subcategory", "category": category_obj.id},
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.data
    assert SubCategory.objects.filter(id=response.data.get("id")).exists()


@pytest.mark.django_db
def test_subcategory_create_already_exists_for_flow_type_fail(
    api_client, subcategory_obj
):
    response = api_client.post(
        reverse("references:subcategory-list"),
        {"name": subcategory_obj.name, "category": subcategory_obj.category.id},
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "id" not in response.data
    assert SubCategory.objects.filter(id=subcategory_obj.id).count() == 1


# retrieve


@pytest.mark.django_db
def test_subcategory_retrieve_success(api_client, subcategory_obj):
    response = api_client.get(
        reverse("references:subcategory-detail", args=[subcategory_obj.id])
    )

    assert response.status_code == status.HTTP_200_OK
    assert "id" in response.data


@pytest.mark.django_db
def test_subcategory_retrieve_not_found_fail(api_client):
    response = api_client.get(reverse("references:subcategory-detail", args=[0]))

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "id" not in response.data


# update


@pytest.mark.django_db
def test_subcategory_update_success(api_client, subcategory_obj):
    response = api_client.patch(
        reverse("references:subcategory-detail", args=[subcategory_obj.id]),
        {"name": "UPDATED"},
    )

    assert response.status_code == status.HTTP_200_OK
    assert "id" in response.data
    subcategory_obj.refresh_from_db()
    assert subcategory_obj.name == "UPDATED"


# delete


@pytest.mark.django_db
def test_subcategory_delete_success(api_client, subcategory_obj):
    response = api_client.delete(
        reverse("references:subcategory-detail", args=[subcategory_obj.id])
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not SubCategory.objects.filter(id=subcategory_obj.id).exists()


@pytest.mark.django_db
def test_subcategory_delete_in_use_fail(api_client, subcategory_obj, record_obj):
    with pytest.raises(ProtectedError):
        api_client.delete(
            reverse("references:subcategory-detail", args=[subcategory_obj.id])
        )

    assert SubCategory.objects.filter(id=subcategory_obj.id).exists()
