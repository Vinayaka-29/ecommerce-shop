from django.contrib import admin
from .models import Category, Product, ProductReview, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'is_available', 'created_at')
    list_filter = ('category', 'is_available', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'stock_quantity', 'is_available')
        }),
        ('Media', {
            'fields': ('image',)
        }),
    )


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at', 'product')
    search_fields = ('product__name', 'user__username')
    readonly_fields = ('created_at', 'updated_at')


class OrderItemInline(admin.TabularInline):
    """Inline admin for OrderItems within Order"""
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price_at_purchase', 'created_at')
    fields = ('product', 'quantity', 'price_at_purchase')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer_name', 'total_amount', 'payment_method', 'status', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('order_id', 'customer_name', 'customer_email', 'customer_phone')
    readonly_fields = ('order_id', 'created_at', 'updated_at', 'get_status_color')
    inlines = [OrderItemInline]
    
    fieldsets = (
        ('Order Information', {
            'fields': ('order_id', 'created_at', 'updated_at')
        }),
        ('Customer Details', {
            'fields': ('customer_name', 'customer_email', 'customer_phone', 'customer_address',
                      'customer_city', 'customer_state', 'customer_pincode', 'customer_country')
        }),
        ('Order Status', {
            'fields': ('status', 'get_status_color', 'payment_method')
        }),
        ('Payment Summary', {
            'fields': ('subtotal', 'tax', 'shipping_cost', 'total_amount')
        }),
    )
    
    def get_status_color(self, obj):
        """Display status with color"""
        color = obj.get_order_status_display_color()
        return f'<span style="color: {color}; font-weight: bold;">{obj.get_status_display()}</span>'
    get_status_color.short_description = 'Status Color'
    get_status_color.allow_tags = True


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price_at_purchase', 'get_item_total', 'created_at')
    list_filter = ('order__status', 'created_at', 'product')
    search_fields = ('order__order_id', 'product__name')
    readonly_fields = ('order', 'product', 'quantity', 'price_at_purchase', 'created_at')
    
    def get_item_total(self, obj):
        """Display item total"""
        return f'₹{obj.get_item_total():.2f}'
    get_item_total.short_description = 'Item Total'
