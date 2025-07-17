from datetime import date

from django.core.validators import MinValueValidator
from django.db import models

from references.models import Category, FlowType, Status, SubCategory
from references.services import ensure_category_consistency

from .validators import validate_date_not_in_future


class CashFlowRecord(models.Model):
    """Model for storing cash flow records."""

    date = models.DateField(
        default=date.today,
        validators=[validate_date_not_in_future],
        help_text="Date of creation of the record "
        "(Optional, If is not specified, will be used today's date)",
    )
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, help_text="Status of the record"
    )
    flow_type = models.ForeignKey(
        FlowType,
        on_delete=models.PROTECT,
        help_text="Type of the cash flow (must match the type in category)",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        help_text="Category of the record (must match the category in subcategory)",
    )
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.PROTECT, help_text="Subcategory of the record"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Amount in rub.",
    )
    comment = models.TextField(blank=True, help_text="Optional Comment")

    def __str__(self) -> str:
        return f"{self.date} - {self.status} - {self.amount} rub."

    def clean(self) -> None:
        ensure_category_consistency(self.flow_type, self.category, self.subcategory)

    class Meta:
        ordering = ["-date"]
        indexes = [
            models.Index(fields=["date"]),
        ]
        verbose_name = "Cash Flow Record"
        verbose_name_plural = "Cash Flow Records"
