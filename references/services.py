from django.core.exceptions import ValidationError

from .models import Category, FlowType, SubCategory


def ensure_category_consistency(
    flow_type: FlowType, category: Category, subcategory: SubCategory
):
    """
    Validates the logical consistency between flow_type, category, and subcategory.
    """
    if category.flow_type != flow_type:
        raise ValidationError(
            {"category": "Category doesn't belong to given flow_type"}
        )

    if subcategory.category != category:
        raise ValidationError(
            {"subcategory": "Subcategory doesn't belong to given category"}
        )
