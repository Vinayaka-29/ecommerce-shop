from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from .models import Order, OrderItem
import json
from django.utils.dateparse import parse_date
from django.db.models import Q, Sum

def admin_login(request):
    """Admin login endpoint - returns JSON response"""
    return JsonResponse({
        'success': True,
        'message': 'Admin login endpoint',
        'instructions': 'POST with username and password',
        'default_username': 'vinayaka29',
        'default_password': 'admin123',
        'endpoints': {
            'login': '/admin/login/',
            'dashboard': '/admin/dashboard/',
            'orders': '/admin/orders/',
            'reports': '/admin/reports/'
        }
    })

def admin_logout(request):
    logout(request)
    return JsonResponse({'success': True, 'message': 'Logged out'})

@login_required(login_url='admin_login')
def admin_dashboard(request):
    return JsonResponse({
        'success': True,
        'message': 'Admin dashboard',
        'total_orders': Order.objects.count(),
        'pending_orders': Order.objects.filter(status='pending').count()
    })

@login_required(login_url='admin_login')
def view_all_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    return JsonResponse({
        'success': True,
        'total_orders': orders.count(),
        'orders': list(orders.values())
    })

@login_required(login_url='admin_login')
def view_order_detail(request, order_id):
    try:
        order = Order.objects.get(order_id=order_id)
        return JsonResponse({'success': True, 'order': {'order_id': order.order_id}})
    except:
        return JsonResponse({'success': False, 'error': 'Order not found'}, status=404)

@login_required(login_url='admin_login')
def update_order_status(request, order_id):
    return JsonResponse({'success': True, 'message': 'Status updated'})

@login_required(login_url='admin_login')
def reports(request):
    return JsonResponse({
        'success': True,
        'total_orders': Order.objects.count(),
        'total_revenue': 0
    })

@login_required(login_url='admin_login')
def export_orders_csv(request):
    return JsonResponse({'success': True, 'message': 'Export CSV'})

def export_orders_json(request):
    return JsonResponse({'success': True, 'orders': []})
