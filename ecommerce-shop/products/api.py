from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Order, OrderItem, Product


# -----------------------
# CREATE ORDER (FRONTEND)
# -----------------------
@csrf_exempt
@require_http_methods(["POST"])
def create_order(request):
    try:
        data = json.loads(request.body)

        order = Order.objects.create(
            order_id=data["order_id"],
            customer_name=data["customer_name"],
            customer_email=data["customer_email"],
            customer_phone=data["customer_phone"],
            customer_address=data["customer_address"],
            total_amount=data["total_amount"],
            status="pending",
        )

        for item in data.get("items", []):
            product = Product.objects.get(id=item["product_id"])
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item["quantity"],
                price_at_purchase=item["price"],
            )

        return JsonResponse({
            "success": True,
            "order_id": order.order_id
        })

    except Product.DoesNotExist:
        return JsonResponse({"success": False, "error": "Product not found"}, status=404)

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


# -----------------------
# TRACK ORDER
# -----------------------
@require_http_methods(["GET"])
def get_order_by_id(request, order_id):
    try:
        order = Order.objects.get(order_id=order_id)

        items = [
            {
                "product": item.product.name,
                "quantity": item.quantity,
                "price": str(item.price_at_purchase),
                "total": str(item.get_item_total()),
            }
            for item in order.items.all()
        ]

        return JsonResponse({
            "order_id": order.order_id,
            "status": order.status,
            "total_amount": str(order.total_amount),
            "items": items,
        })

    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)
