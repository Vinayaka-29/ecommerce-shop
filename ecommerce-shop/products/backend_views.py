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

# =======================
# ADMIN AUTHENTICATION
# =======================

@csrf_protect
@require_http_methods(["GET", "POST"])
def admin_login(request):
    """
    Admin login API endpoint
    Default credentials: username=vinayaka29, password=admin123
    """
    if request.user.is_authenticated and request.user.is_staff:
        return JsonResponse({'success': True, 'message': 'Already logged in', 'username': request.user.username})
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
        except:
            username = request.POST.get('username')
            password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            return JsonResponse({
                'success': True,
                'message': 'Login successful',
                'username': user.username,
                'user_id': user.id
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Invalid credentials or not an admin user',
                'error': 'Authentication failed'
            }, status=401)
    
    # For GET request, return login instructions
    return JsonResponse({
        'message': 'Admin Login API',
        'instructions': 'Send POST request with username and password',
        'default_credentials': {'username': 'vinayaka29', 'password': 'admin123'},
        'endpoint': '/admin/login/',
        'method': 'POST',
        'example': {
            'username': 'vinayaka29',
            'password': 'admin123'
        }
    })

def admin_logout(request):
    """
    Admin logout view
    """
    logout(request)
    return JsonResponse({'success': True, 'message': 'Logged out successfully'})

# =======================
# ADMIN DASHBOARD
# =======================

@login_required(login_url='admin_login')
def admin_dashboard(request):
    """
    Main admin dashboard API returning order statistics
    """
    if not request.user.is_staff:
        return JsonResponse({'success': False, 'error': 'Unauthorized - Admin access required'}, status=403)
    
    # Get statistics
    total_orders = Order.objects.count()
    pending_orders = Order.objects.filter(status='pending').count()
    confirmed_orders = Order.objects.filter(status='confirmed').count()
    shipped_orders = Order.objects.filter(status='shipped').count()
    delivered_orders = Order.objects.filter(status='delivered').count()
    cancelled_orders = Order.objects.filter(status='cancelled').count()
    
    # Calculate total revenue
    total_revenue = Order.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    
    # Get recent orders
    recent_orders = list(Order.objects.all().order_by('-created_at')[:10].values())
    
    return JsonResponse({
        'success': True,
        'admin_dashboard': {
            'total_orders': total_orders,
            'pending_orders': pending_orders,
            'confirmed_orders': confirmed_orders,
            'shipped_orders': shipped_orders,
            'delivered_orders': delivered_orders,
            'cancelled_orders': cancelled_orders,
            'total_revenue': float(total_revenue),
            'recent_orders': recent_orders,
            'username': request.user.username
        }
    })

# =======================
# ORDER MANAGEMENT
# =======================

@login_required(login_url='admin_login')
def view_all_orders(request):
    """
    View all orders with filtering and search capabilities
    """
    if not request.user.is_staff:
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)
    
    orders = Order.objects.all().order_by('-created_at')
    
    # Filter by status
    status_filter = request.GET.get('status')
    if status_filter:
        orders = orders.filter(status=status_filter)
    
    # Filter by payment method
    payment_filter = request.GET.get('payment')
    if payment_filter:
        orders = orders.filter(payment_method=payment_filter)
    
    # Search by order ID, customer name, or email
    search_query = request.GET.get('search')
    if search_query:
        orders = orders.filter(
            Q(order_id__icontains=search_query) |
            Q(customer_name__icontains=search_query) |
            Q(customer_email__icontains=search_query) |
            Q(customer_phone__icontains=search_query)
        )
    
    orders_data = list(orders.values())
    
    return JsonResponse({
        'success': True,
        'total_count': len(orders_data),
        'orders': orders_data,
        'filters': {
            'status': status_filter,
            'payment': payment_filter,
            'search': search_query
        }
    })

@login_required(login_url='admin_login')
def view_order_detail(request, order_id):
    """
    View detailed information about a specific order
    """
    if not request.user.is_staff:
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)
    
    try:
        order = Order.objects.get(order_id=order_id)
        items = list(order.items.all().values())
        
        order_data = {
            'order_id': order.order_id,
            'customer_name': order.customer_name,
            'customer_email': order.customer_email,
            'customer_phone': order.customer_phone,
            'customer_address': order.customer_address,
            'customer_city': order.customer_city,
            'customer_state': order.customer_state,
            'customer_pincode': order.customer_pincode,
            'customer_country': order.customer_country,
            'total_amount': float(order.total_amount),
            'payment_method': order.payment_method,
            'status': order.status,
            'created_at': order.created_at.isoformat(),
            'updated_at': order.updated_at.isoformat(),
            'items': items
        }
        
        return JsonResponse({
            'success': True,
            'order': order_data
        })
    except Order.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Order not found'}, status=404)

@login_required(login_url='admin_login')
@require_http_methods(["POST"])
def update_order_status(request, order_id):
    """
    Update order status via API
    """
    if not request.user.is_staff:
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)
    
    try:
        order = Order.objects.get(order_id=order_id)
        
        try:
            data = json.loads(request.body)
            new_status = data.get('status')
        except:
            new_status = request.POST.get('status')
        
        valid_statuses = ['pending', 'confirmed', 'shipped', 'delivered', 'cancelled']
        if new_status not in valid_statuses:
            return JsonResponse({'success': False, 'error': 'Invalid status'})
        
        order.status = new_status
        order.save()
        
        return JsonResponse({
            'success': True,
            'message': f'Order {order_id} status updated to {new_status}'
        })
    except Order.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Order not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

# =======================
# ADMIN REPORTS
# =======================

@login_required(login_url='admin_login')
def reports(request):
    """
    Admin reports and analytics API
    """
    if not request.user.is_staff:
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)
    
    # Overall statistics
    total_orders = Order.objects.count()
    total_revenue = Order.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    
    # Status breakdown
    status_breakdown = {}
    for status in ['pending', 'confirmed', 'shipped', 'delivered', 'cancelled']:
        status_breakdown[status] = Order.objects.filter(status=status).count()
    
    # Payment method breakdown
    payment_breakdown = {}
    for method in ['credit_card', 'debit_card', 'paypal', 'upi', 'net_banking']:
        payment_breakdown[method] = Order.objects.filter(payment_method=method).count()
    
    # Top selling products
    top_products = list(OrderItem.objects.values('product__name').annotate(
        total_quantity=Sum('quantity')
    ).order_by('-total_quantity')[:5])
    
    return JsonResponse({
        'success': True,
        'reports': {
            'total_orders': total_orders,
            'total_revenue': float(total_revenue),
            'status_breakdown': status_breakdown,
            'payment_breakdown': payment_breakdown,
            'top_products': top_products
        }
    })

# =======================
# EXPORT DATA
# =======================

@login_required(login_url='admin_login')
def export_orders_csv(request):
    """
    Export all orders to CSV format
    """
    if not request.user.is_staff:
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)
    
    import csv
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'
    
    writer = csv.writer(response)
    writer.writerow([
        'Order ID', 'Customer Name', 'Email', 'Phone', 'Total Amount',
        'Payment Method', 'Status', 'Created At', 'Updated At'
    ])
    
    orders = Order.objects.all().order_by('-created_at')
    for order in orders:
        writer.writerow([
            order.order_id,
            order.customer_name,
            order.customer_email,
            order.customer_phone,
            order.total_amount,
            order.payment_method,
            order.status,
            order.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            order.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        ])
    
    return response

@login_required(login_url='admin_login')
def export_orders_json(request):
    """
    Export all orders to JSON format
    """
    if not request.user.is_staff:
        return JsonResponse({'success': False, 'error': 'Unauthorized'}, status=403)
    
    orders = Order.objects.all().order_by('-created_at')
    
    orders_data = []
    for order in orders:
        items = order.items.all()
        items_data = [{
            'product_name': item.product.name,
            'quantity': item.quantity,
            'price_at_purchase': str(item.price_at_purchase),
            'item_total': str(item.get_item_total())
        } for item in items]
        
        orders_data.append({
            'order_id': order.order_id,
            'customer_name': order.customer_name,
            'customer_email': order.customer_email,
            'customer_phone': order.customer_phone,
            'customer_address': order.customer_address,
            'customer_city': order.customer_city,
            'customer_state': order.customer_state,
            'customer_pincode': order.customer_pincode,
            'customer_country': order.customer_country,
            'total_amount': str(order.total_amount),
            'payment_method': order.payment_method,
            'status': order.status,
            'created_at': order.created_at.isoformat(),
            'updated_at': order.updated_at.isoformat(),
            'items': items_data
        })
    
    response = HttpResponse(
        json.dumps(orders_data, indent=2),
        content_type='application/json'
    )
    response['Content-Disposition'] = 'attachment; filename="orders.json"'
    
    return response
