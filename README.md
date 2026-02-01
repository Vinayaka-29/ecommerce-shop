# E-Commerce Shop 🛒

A full-featured Django e-commerce platform with product catalog, shopping cart, user authentication, and order management.

## 🌐 Live Demo

**Repository**: [https://github.com/Vinayaka-29/ecommerce-shop](https://github.com/Vinayaka-29/ecommerce-shop)
> **Note**: GitHub Pages hosts static files. For full Django functionality with database and cart features, deploy to PythonAnywhere or Render (see Deployment section below).


## 🌟 Features

- 🛋️ **Product Catalog** - Browse products with images, descriptions, and prices
- 🛒 **Shopping Cart** - Add/remove items, update quantities
- 🔐 **User Authentication** - Register, login, and manage profile
- 🔍 **Search & Filter** - Find products by category, price, or name
- 📦 **Order Management** - Track orders and order history  
- 👨‍💻 **Admin Panel** - Manage products, orders, and users

## 🚀 Technologies Used

- **Backend**: Django 4.x
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Authentication**: Django Built-in Auth
- **Payment**: Stripe integration ready

## 📁 Project Structure

```
ecommerce-shop/
├── shop/                  # Main Django project
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI config
├── products/             # Products app
│   ├── models.py         # Product, Category, Review models
│   ├── views.py          # Product views
│   └── templates/        # Product templates
├── cart/                 # Shopping cart app
├── orders/               # Order management
├── static/               # Static files (CSS, JS, images)
├── media/                # User uploaded files
├── templates/            # Base templates
├── manage.py             # Django management
├── requirements.txt      # Python dependencies
└── DEPLOYMENT.md         # Deployment guide
```

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip
- virtualenv (recommended)

### Quick Start

```bash
# Navigate to project
cd ecommerce-shop

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

**Access at**: http://localhost:8000/
**Admin panel**: http://localhost:8000/admin/

## 📦 Database Models

### Product Model
- Category, name, slug
- Description, price, image
- Stock quantity, availability
- Timestamps

### Order Model  
- User, order number
- Total amount, status
- Shipping address
- Created/updated dates

### Cart Model
- User/session
- Items (many-to-many with Product)
- Quantities

## 🌐 Deployment

For deployment instructions to production platforms (Render, PythonAnywhere, Railway, Heroku), see [DEPLOYMENT.md](ecommerce-shop/DEPLOYMENT.md)

### Quick Deploy Options:
- **Render.com** (FREE) - https://render.com
- **PythonAnywhere** (FREE) - https://www.pythonanywhere.com
- **Railway** (FREE) - https://railway.app

## 🔐 Security Features

- CSRF protection
- Password hashing
- SQL injection protection
- XSS prevention
- Secure session management

## 💡 Key Features Explained

### Product Management
- Admin interface for product CRUD
- Category organization
- Image upload support
- Stock tracking

### Shopping Experience
- Responsive product catalog
- Product search and filtering
- Quick add to cart
- Cart summary with totals

### Checkout Process
- Secure checkout flow
- Shipping address management
- Order review before purchase
- Order confirmation

## 🚀 Future Enhancements

- [ ] Payment gateway integration (Stripe/PayPal/Razorpay)
- [ ] Product reviews and ratings
- [ ] Wishlist functionality
- [ ] Advanced search with filters
- [ ] Email notifications
- [ ] Discount codes/coupons
- [ ] Multi-vendor support
- [ ] Real-time inventory updates
- [ ] Order tracking
- [ ] Product recommendations

## 📝 License

MIT License - free to use for learning purposes

## 👤 Author

**Vinayaka-29**
- GitHub: [@Vinayaka-29](https://github.com/Vinayaka-29)
- Repository: [ecommerce-shop](https://github.com/Vinayaka-29/ecommerce-shop)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

**Note**: This is a learning project demonstrating Django e-commerce concepts. For production use, implement additional security measures and payment integration.

**Happy Shopping!** 🛒🎉
