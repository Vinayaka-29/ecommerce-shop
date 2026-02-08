# E-Commerce Shop Admin API Documentation

## Overview

This document describes the Admin Backend API endpoints for managing orders in the e-commerce platform. All API endpoints require authentication via token-based authentication.

## Authentication

### Token-Based Authentication

All API endpoints require a Bearer token to be included in the Authorization header:

```
Authorization: Bearer <token>
```

**Default Admin Token:** `vinayaka29_admin_token_2024`

**Example Request:**
```bash
curl -H "Authorization: Bearer vinayaka29_admin_token_2024" \
  http://localhost:8000/api/orders/
```

## API Endpoints

### 1. Get All Orders

**Endpoint:** `GET /api/orders/`

**Description:** Retrieve all orders from the system

**Headers:**
```
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "success": true,
  "total_orders": 5,
  "orders": [
    {
      "id": 1,
      "order_id": "ORD-2025-001",
      "customer_name": "John Doe",
      "customer_email": "john@example.com",
      "customer_phone": "9876543210",
      "customer_address": "123 Main Street",
      "customer_city": "Bangalore",
      "customer_state": "Karnataka",
      "customer_pincode": "560001",
      "customer_country": "India",
      "subtotal": "999.99",
      "tax": "179.99",
      "shipping_cost": "50.00",
      "total_amount": "1229.98",
      "payment_method": "card",
      "status": "pending",
      "created_at": "2025-02-08T12:30:00Z",
      "updated_at": "2025-02-08T12:30:00Z",
      "items": [
        {
          "product_name": "Laptop",
          "quantity": 1,
          "price_at_purchase": "999.99",
          "item_total": "999.99"
        }
      ]
    }
  ]
}
```

### 2. Get Order by ID

**Endpoint:** `GET /api/orders/<order_id>/`

**Description:** Retrieve a specific order by order_id

**Parameters:**
- `order_id` (string, path): The order ID to retrieve

**Example:**
```bash
curl -H "Authorization: Bearer vinayaka29_admin_token_2024" \
  http://localhost:8000/api/orders/ORD-2025-001/
```

**Response (200 OK):**
```json
{
  "success": true,
  "order": {
    "id": 1,
    "order_id": "ORD-2025-001",
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "total_amount": "1229.98",
    "payment_method": "card",
    "status": "pending",
    "items": [...]
  }
}
```

### 3. Get Orders by Status

**Endpoint:** `GET /api/orders/status/<status>/`

**Description:** Filter orders by status

**Parameters:**
- `status` (string, path): One of: `pending`, `confirmed`, `shipped`, `delivered`, `cancelled`

**Example:**
```bash
curl -H "Authorization: Bearer vinayaka29_admin_token_2024" \
  http://localhost:8000/api/orders/status/pending/
```

**Response (200 OK):**
```json
{
  "success": true,
  "status_filter": "pending",
  "total_orders": 3,
  "orders": [...]
}
```

### 4. Update Order Status

**Endpoint:** `POST /api/orders/<order_id>/update-status/`

**Description:** Update the status of an order

**Parameters:**
- `order_id` (string, path): The order ID to update

**Request Body:**
```json
{
  "status": "confirmed"
}
```

**Valid Statuses:** `pending`, `confirmed`, `shipped`, `delivered`, `cancelled`

**Example:**
```bash
curl -X POST \
  -H "Authorization: Bearer vinayaka29_admin_token_2024" \
  -H "Content-Type: application/json" \
  -d '{"status": "shipped"}' \
  http://localhost:8000/api/orders/ORD-2025-001/update-status/
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Order ORD-2025-001 status updated to shipped",
  "order_id": "ORD-2025-001",
  "new_status": "shipped"
}
```

### 5. Get Order Statistics

**Endpoint:** `GET /api/orders/statistics/`

**Description:** Get aggregated order statistics for analytics

**Example:**
```bash
curl -H "Authorization: Bearer vinayaka29_admin_token_2024" \
  http://localhost:8000/api/orders/statistics/
```

**Response (200 OK):**
```json
{
  "success": true,
  "statistics": {
    "total_orders": 10,
    "total_revenue": "9999.99",
    "status_breakdown": {
      "pending": 2,
      "confirmed": 3,
      "shipped": 2,
      "delivered": 2,
      "cancelled": 1
    },
    "payment_method_breakdown": {
      "cod": 5,
      "upi": 3,
      "card": 2
    }
  }
}
```

## Error Responses

### 401 Unauthorized

```json
{
  "success": false,
  "error": "Missing or invalid authorization header. Use: Authorization: Bearer <token>"
}
```

### 403 Forbidden

```json
{
  "success": false,
  "error": "Invalid authentication token"
}
```

### 404 Not Found

```json
{
  "success": false,
  "error": "Order not found"
}
```

### 400 Bad Request

```json
{
  "success": false,
  "error": "Invalid status. Valid statuses: ['pending', 'confirmed', 'shipped', 'delivered', 'cancelled']"
}
```

### 500 Internal Server Error

```json
{
  "success": false,
  "error": "Error message describing the issue"
}
```

## Admin Backend Views

### Admin Login

**URL:** `/admin/login/`

**Method:** GET, POST

**Description:** Admin login page and authentication

**Default Credentials:**
- **Username:** vinayaka29
- **Password:** admin123

### Admin Dashboard

**URL:** `/admin/dashboard/`

**Method:** GET

**Description:** Main admin dashboard with order statistics

**Requires Authentication:** Yes (staff user)

### View All Orders

**URL:** `/admin/orders/`

**Method:** GET

**Description:** View all orders with filtering and search

**Query Parameters:**
- `status` (optional): Filter by status
- `payment` (optional): Filter by payment method
- `search` (optional): Search by order ID, customer name, email, or phone

### View Order Detail

**URL:** `/admin/orders/<order_id>/`

**Method:** GET

**Description:** View detailed information about a specific order

### Update Order Status (Dashboard)

**URL:** `/admin/orders/<order_id>/update-status/`

**Method:** POST

**Description:** Update order status from admin dashboard

### Admin Reports

**URL:** `/admin/reports/`

**Method:** GET

**Description:** View analytics and reports with detailed breakdowns

### Export Orders as CSV

**URL:** `/admin/orders/export-csv/`

**Method:** GET

**Description:** Download all orders as CSV file

### Export Orders as JSON

**URL:** `/admin/orders/export-json/`

**Method:** GET

**Description:** Download all orders as JSON file

## Setting Up the Admin User

### Create Admin User (Django Management Command)

```bash
cd ecommerce-shop
python manage.py createsuperuser
# Enter username: vinayaka29
# Enter email: admin@example.com
# Enter password: admin123
# Enter password (again): admin123
```

### Access Django Admin

**URL:** `http://localhost:8000/admin/`

**Username:** vinayaka29

**Password:** admin123

## Integration Examples

### JavaScript/Fetch API

```javascript
// Get all orders
fetch('http://localhost:8000/api/orders/', {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer vinayaka29_admin_token_2024',
    'Content-Type': 'application/json'
  }
})
.then(response => response.json())
.then(data => console.log(data));

// Update order status
fetch('http://localhost:8000/api/orders/ORD-2025-001/update-status/', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer vinayaka29_admin_token_2024',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ status: 'shipped' })
})
.then(response => response.json())
.then(data => console.log(data));
```

### Python/Requests

```python
import requests

headers = {
    'Authorization': 'Bearer vinayaka29_admin_token_2024',
    'Content-Type': 'application/json'
}

# Get all orders
response = requests.get('http://localhost:8000/api/orders/', headers=headers)
print(response.json())

# Update order status
response = requests.post(
    'http://localhost:8000/api/orders/ORD-2025-001/update-status/',
    headers=headers,
    json={'status': 'shipped'}
)
print(response.json())
```

## Security Notes

1. **Token Security:** Keep your authentication token private and secure.
2. **HTTPS:** Always use HTTPS in production to encrypt credentials.
3. **CORS:** Configure CORS headers appropriately for your frontend domain.
4. **Rate Limiting:** Consider implementing rate limiting for API endpoints.
5. **Audit Logging:** Log all admin actions for security and compliance.

## Version History

- **v1.0.0** (2025-02-08): Initial release with admin API endpoints and backend views

## Support

For issues or questions, please refer to the main README.md or contact the development team.
