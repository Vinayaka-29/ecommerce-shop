from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from products import backend_views
from products import api
from products.views import product_list   # ✅ ADD THIS


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Website pages
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('products/', product_list, name='products'),  # ✅ THIS WAS MISSING
    path('cart.html', TemplateView.as_view(template_name='cart.html'), name='cart'),
    path('checkout.html', TemplateView.as_view(template_name='checkout.html'), name='checkout'),
    path('bill.html', TemplateView.as_view(template_name='bill.html'), name='bill'),

    # Admin Backend URLs
    path('admin/login/', backend_views.admin_login, name='admin_login'),
    path('admin/dashboard/', backend_views.admin_dashboard, name='admin_dashboard'),
    path('admin/orders/', backend_views.view_all_orders, name='view_all_orders'),
    path('admin/orders/<str:order_id>/', backend_views.view_order_detail, name='view_order_detail'),
    path('admin/reports/', backend_views.reports, name='admin_reports'),
    path('admin/orders/export-csv/', backend_views.export_orders_csv, name='export_orders_csv'),
    path(
        'admin/orders/<str:order_id>/update-status/',
        backend_views.update_order_status,
        name='update_order_status_view'
    ),

    # API Endpoints
    path('api/orders/', api.get_all_orders, name='api_get_all_orders'),
    path('api/orders/<str:order_id>/', api.get_order_by_id, name='api_get_order_detail'),
    path('api/orders/status/<str:status>/', api.get_orders_by_status, name='api_get_orders_by_status'),
    path('api/orders/<str:order_id>/update-status/', api.update_order_status, name='api_update_order_status'),
    path('api/orders/statistics/', api.get_order_statistics, name='api_get_statistics'),
]

# Static + Media files (Render / production)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
