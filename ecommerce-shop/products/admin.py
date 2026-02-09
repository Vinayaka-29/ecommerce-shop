from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name",)
    ordering = ("-created_at",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer_name",
        "customer_email",
        "product",
        "quantity",
        "ordered_at",
    )
    list_filter = ("ordered_at",)
    search_fields = ("customer_name", "customer_email")
    ordering = ("-ordered_at",)
