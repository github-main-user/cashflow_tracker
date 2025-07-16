from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f"Status: {self.name}"


class FlowType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f"FlowType: {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    flow_type = models.ForeignKey(FlowType, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Category: {self.name} for {self.flow_type.name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("name", "flow_type"), name="unique_category_per_flow_type"
            )
        ]


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"SubCategory: {self.name} for {self.category.name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("name", "category"), name="unique_subcategory_per_category"
            )
        ]
