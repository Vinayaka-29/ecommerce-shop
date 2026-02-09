from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("backend/", views.dashboard),
    path("backend/products/", views.products),
    path("backend/products/add/", views.add_product),
    path("backend/orders/", views.orders),
]
