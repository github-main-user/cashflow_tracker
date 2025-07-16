from django.contrib import admin

from .models import Category, FlowType, Status, SubCategory


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(FlowType)
class FlowTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "flow_type")
    search_fields = ("name", "flow_type")
    list_filter = ("flow_type",)
    autocomplete_fields = ("flow_type",)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    search_fields = ("name", "category")
    list_filter = ("category",)
    autocomplete_fields = ("category",)
