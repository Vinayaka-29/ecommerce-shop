from django.http import JsonResponse
from .models import Order, OrderItem, Product
import json

def create_order(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    data = json.loads(request.body)

    order = Order.objects.create(
        customer_name=data["customer_name"],
        customer_email=data["customer_email"],
        customer_phone=data["customer_phone"],
        customer_address=data["customer_address"],
        total_amount=data["total_amount"],
        payment_method=data.get("payment_method", "cod"),
    )

    for item in data["items"]:
        product = Product.objects.get(id=item["product_id"])
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=item["quantity"],
            price_at_purchase=product.price,
        )

    return JsonResponse({
        "success": True,
        "order_id": order.id
    })
