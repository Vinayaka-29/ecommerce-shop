from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from products import backend_views

urlpatterns = [
    path('admin/', admin.site.urls),

        path('', TemplateView.as_view(template_name='index.html'), name='home'),
        path('cart.html', TemplateView.as_view(template_name='cart.html'), name='cart'),
    path('checkout.html', TemplateView.as_view(template_name='checkout.html'), name='checkout'),
    path('bill.html', TemplateView.as_view(template_name='bill.html'), name='bill'),
        # Admin Backend URLs
    path('admin/login/', backend_views.admin_login, name='admin_login'),
    path('admin/dashboard/', backend_views.admin_dashboard, name='admin_dashboard'),
    path('admin/orders/', backend_views.view_all_orders, name='view_all_orders'),
    path('admin/orders/<int:order_id>/', backend_views.view_order_detail, name='view_order_detail'),
    path('admin/reports/', backend_views.reports, name='admin_reports'),    path('admin/orders/export-csv/', backend_views.export_orders_csv, name='export_orders_csv'),
    path('admin/orders/export-json/', backend_views.export_orders_json, name='export_orders_json'),
    ]
        # Order Management API Endpoints

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
