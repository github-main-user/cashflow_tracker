from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from references.models import Category, FlowType, Status, SubCategory


class CashFlowRecord(models.Model):
    date = models.DateField(default=date.today)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    flow_type = models.ForeignKey(FlowType, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    comment = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"CashFlowRecord: {self.date} - {self.status} - {self.amount} rub."

    def clean(self) -> None:
        if self.category.flow_type != self.flow_type:
            raise ValidationError(
                {"category": "Category doesn't belong to given flow_type"}
            )

        if self.subcategory.category != self.category:
            raise ValidationError(
                {"subcategory": "Subcategory doesn't belong to given category"}
            )

    class Meta:
        ordering = ["-date"]
        indexes = [
            models.Index(fields=["date"]),
        ]

