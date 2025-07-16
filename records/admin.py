from django.contrib import admin

from .models import CashFlowRecord


@admin.register(CashFlowRecord)
class CashFlowRecordAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "status",
        "flow_type",
        "category",
        "subcategory",
        "amount",
        "comment",
    )
    search_fields = ("comments",)
    list_filter = ("status", "flow_type", "category", "subcategory")
    ordering = ("date",)
    date_hierarchy = "date"
    autocomplete_fields = ("category", "subcategory")
