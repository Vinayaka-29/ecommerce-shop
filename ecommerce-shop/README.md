# E-Commerce Shop 🛒

A mini Amazon-style e-commerce website built with Django.

## 📋 Features

- **Product Catalog** - Browse products with images, descriptions, and prices
- **Shopping Cart** - Add/remove items, update quantities
- **User Authentication** - Register, login, and manage profile
- **Search & Filter** - Find products by category, price, or name
- **Order Management** - Track orders and order history
- **Admin Panel** - Manage products, orders, and users

## 🚀 Technologies Used

- **Backend**: Django 4.x
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Authentication**: Django Built-in Auth

## 📁 Project Structure

```
ecommerce-shop/
├── shop/                  # Main Django project
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI config
├── products/             # Products app
│   ├── models.py         # Product, Category models
│   ├── views.py          # Product views
│   └── templates/        # Product templates
├── cart/                 # Shopping cart app
│   ├── models.py         # Cart models
│   ├── views.py          # Cart views
│   └── templates/        # Cart templates
├── orders/               # Order management
│   ├── models.py         # Order models
│   ├── views.py          # Order views
│   └── templates/        # Order templates
├── static/               # Static files (CSS, JS, images)
├── media/                # User uploaded files
├── templates/            # Base templates
├── manage.py             # Django management
└── requirements.txt      # Python dependencies
```

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

### Installation Steps

1. **Clone the repository**
```bash
cd ecommerce-shop
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```

6. **Load sample data (optional)**
```bash
python manage.py loaddata sample_data.json
```

7. **Run development server**
```bash
python manage.py runserver
```

8. **Access the application**
- Main site: http://localhost:8000/
- Admin panel: http://localhost:8000/admin/

## 💡 Key Features Explained

### Product Management
- Admin can add/edit/delete products
- Products organized by categories
- Product images and detailed descriptions
- Stock management

### Shopping Cart
- Session-based cart for guests
- Persistent cart for logged-in users
- Real-time price calculations
- Cart summary with totals

### User Accounts
- Registration with email verification
- Login/logout functionality
- User profile management
- Order history

### Checkout Process
- Shipping address management
- Order summary review
- Payment integration ready
- Order confirmation emails

## 📦 Database Models

### Product Model
- name, description, price
- category, image
- stock_quantity, is_available
- created_at, updated_at

### Order Model
- user, order_number
- total_amount, status
- shipping_address
- created_at

### Cart Model
- user/session
- items (many-to-many with Product)
- quantities

## 🎨 Frontend

- Responsive design (mobile-friendly)
- Bootstrap components
- AJAX for cart operations
- Product image gallery
- Search autocomplete

## 🔐 Security Features

- CSRF protection
- Password hashing
- SQL injection protection
- XSS prevention
- Secure session management

## 🚧 Future Enhancements

- [ ] Payment gateway integration (Stripe/PayPal)
- [ ] Product reviews and ratings
- [ ] Wishlist functionality
- [ ] Advanced search filters
- [ ] Email notifications
- [ ] Discount codes/coupons
- [ ] Multi-vendor support
- [ ] Real-time inventory updates

## 📝 License

MIT License - feel free to use this project for learning purposes

## 👨‍💻 Author

Vinayaka-29

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

**Note**: This is a learning project demonstrating Django e-commerce concepts. For production use, additional security measures and payment integration would be required.
