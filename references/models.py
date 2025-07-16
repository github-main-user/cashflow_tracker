from django.db import models


class Status(models.Model):
    """Model for storing cash flow record status."""

    name = models.CharField(max_length=100, unique=True, help_text="Name of the status")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class FlowType(models.Model):
    """Model for storing cash flow type."""

    name = models.CharField(
        max_length=100, unique=True, help_text="Name of the cash flow type"
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Flow Type"
        verbose_name_plural = "Flow Types"


class Category(models.Model):
    """Model for storing cash flow record category."""

    name = models.CharField(max_length=100, help_text="Name of the category")
    flow_type = models.ForeignKey(
        FlowType, on_delete=models.CASCADE, help_text="Connected cash flow type"
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("name", "flow_type"), name="unique_category_per_flow_type"
            )
        ]
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    """Model for storing cash flow record subcategory."""

    name = models.CharField(max_length=100, help_text="Name of the subcategory")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, help_text="Connected category"
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("name", "category"), name="unique_subcategory_per_category"
            )
        ]
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"
