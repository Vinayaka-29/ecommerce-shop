# Admin Setup & Deployment Guide

Complete step-by-step guide to create an admin account, run the website locally, and deploy it live.

---

## 🔧 PART 1: LOCAL SETUP & ADMIN CREATION

### Step 1: Clone the Repository

```bash
git clone https://github.com/Vinayaka-29/ecommerce-shop.git
cd ecommerce-shop
```

### Step 2: Navigate to Project Directory

```bash
cd ecommerce-shop
```

### Step 3: Create Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run Database Migrations

```bash
python manage.py migrate
```

This creates the database and tables for orders, products, etc.

### Step 6: Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

**Enter the following information:**

```
Username: admin
Email: admin@ecommerce.com
Password: AdminPassword123  (Use strong password!)
Password (again): AdminPassword123
```

**Example:**
```
Username: admin
Email address: your-email@gmail.com
Password: 
**don’t share your password!!**
Password (again): 
Superuser created successfully.
```

### Step 7: Run Development Server

```bash
python manage.py runserver
```

**Output:**
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

---

## 🌐 PART 2: ACCESS THE WEBSITE LOCALLY

### Open in Browser:

1. **Homepage**: http://127.0.0.1:8000/
2. **Admin Panel**: http://127.0.0.1:8000/admin/
   - Username: `admin`
   - Password: `AdminPassword123` (or your password)

3. **Place Order**: http://127.0.0.1:8000/checkout.html
4. **Track Order**: http://127.0.0.1:8000/order-tracking/

### View Orders in Admin:

1. Go to http://127.0.0.1:8000/admin/
2. Login with credentials
3. Click **"Orders"** in the left sidebar
4. See all orders placed
5. Click any order to view/edit details

---

## 🚀 PART 3: DEPLOY LIVE (PRODUCTION)

### Option A: Deploy to PythonAnywhere (Easiest)

#### Step 1: Create PythonAnywhere Account
- Go to https://www.pythonanywhere.com/
- Sign up for free account

#### Step 2: Add Web App
1. Dashboard → "Add a new web app"
2. Choose Python 4.2 and Django
3. Select `/home/your-username/ecommerce-shop`

#### Step 3: Clone Repository

In PythonAnywhere Bash Console:

```bash
cd /home/your-username
git clone https://github.com/Vinayaka-29/ecommerce-shop.git
cd ecommerce-shop/ecommerce-shop
```

#### Step 4: Create Virtual Environment on PythonAnywhere

```bash
mkvirtualenv --python=/usr/bin/python3.9 mysite
workon mysite
pip install -r requirements.txt
```

#### Step 5: Configure WSGI File

Edit `/var/www/your-username_pythonanywhere_com_wsgi.py`:

```python
import os
import sys

path = '/home/your-username/ecommerce-shop/ecommerce-shop'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'shop.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### Step 6: Set Up Database

In PythonAnywhere Bash Console:

```bash
cd /home/your-username/ecommerce-shop/ecommerce-shop
workon mysite
python manage.py migrate
python manage.py createsuperuser
```

Create admin account:
```
Username: admin
Email: your-email@gmail.com
Password: YourSecurePassword
```

#### Step 7: Reload Web App

1. Go to Web tab
2. Click "Reload"
3. Visit your-username.pythonanywhere.com

---

### Option B: Deploy to Render.com (Alternative)

#### Step 1: Create Render Account
- Go to https://render.com
- Sign up

#### Step 2: Create New Web Service
1. Dashboard → New Web Service
2. Connect your GitHub repository
3. Select `ecommerce-shop` repo
4. Build command: `pip install -r ecommerce-shop/requirements.txt && python ecommerce-shop/manage.py migrate`
5. Start command: `gunicorn shop.wsgi:application --bind 0.0.0.0:$PORT`

#### Step 3: Set Environment Variables

Add in Render dashboard:
```
KEY: ALLOWED_HOSTS
VALUE: your-app.onrender.com, localhost

KEY: DEBUG
VALUE: False
```

#### Step 4: Create Admin Account

In Render Shell (after deployment):

```bash
python manage.py createsuperuser
```

Enter:
```
Username: admin
Email: admin@ecommerce.com
Password: StrongPassword123
```

#### Step 5: Access Your App

- **Website**: https://your-app.onrender.com/
- **Admin**: https://your-app.onrender.com/admin/

---

### Option C: Deploy to Heroku (If Still Available)

#### Step 1: Install Heroku CLI
```bash
https://devcenter.heroku.com/articles/heroku-cli
```

#### Step 2: Login to Heroku
```bash
heroku login
```

#### Step 3: Create App
```bash
heroku create your-ecommerce-app
```

#### Step 4: Deploy Code
```bash
git push heroku main
```

#### Step 5: Run Migrations
```bash
heroku run python manage.py migrate
```

#### Step 6: Create Superuser
```bash
heroku run python manage.py createsuperuser
```

#### Step 7: Open App
```bash
heroku open
```

---

## 📊 VERIFICATION CHECKLIST

### Local Setup
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (pip install -r requirements.txt)
- [ ] Database migrated (python manage.py migrate)
- [ ] Superuser created (python manage.py createsuperuser)
- [ ] Server running (python manage.py runserver)
- [ ] Can access http://127.0.0.1:8000/ 
- [ ] Can login to http://127.0.0.1:8000/admin/
- [ ] Can see Orders in admin panel

### Production Deployment
- [ ] Repository connected to hosting platform
- [ ] Environment variables configured
- [ ] Database migrations completed
- [ ] Superuser created on production
- [ ] Static files collected (python manage.py collectstatic)
- [ ] Website accessible at live URL
- [ ] Admin panel accessible at /admin/
- [ ] Can place and track orders

---

## 🔐 IMPORTANT SECURITY NOTES

1. **DEBUG = False** in production
2. Use **strong passwords** for admin accounts
3. **ALLOWED_HOSTS** must include your domain
4. Use **SECRET_KEY** environment variable
5. Enable **HTTPS** (automatic on most platforms)
6. Keep **Django updated**
7. Use environment variables for sensitive data

---

## 📧 DEFAULT ADMIN CREDENTIALS (CHANGE THESE!)

**After creating admin account, first login and:**
1. Go to http://your-website/admin/
2. Click on your username (top right)
3. Change password to something secure
4. Update email address if needed

---

## 🆘 TROUBLESHOOTING

### Issue: "Port 8000 already in use"
```bash
python manage.py runserver 8001
```

### Issue: "No module named django"
```bash
pip install -r requirements.txt
```

### Issue: Database errors after deployment
```bash
python manage.py migrate --run-syncdb
```

### Issue: Can't login to admin
- Check username/password
- Reset with: `python manage.py changepassword admin`

### Issue: Orders not showing in admin
- Check if migrations ran: `python manage.py migrate`
- Verify Order model registered in admin.py

---

## 📚 USEFUL COMMANDS

```bash
# Start server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Reset superuser password
python manage.py changepassword admin

# Run migrations
python manage.py migrate

# Make migrations (if model changed)
python manage.py makemigrations

# Collect static files (production)
python manage.py collectstatic

# Shell (test queries)
python manage.py shell

# Delete database and start fresh
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---

## ✅ NEXT STEPS

1. Follow PART 1 to create admin account locally
2. Test website locally for 24 hours
3. Place test orders to verify flow
4. Choose hosting platform (Option A, B, or C)
5. Deploy to production
6. Create production admin account
7. Test live website
8. Share with users!

---

## 💡 TIPS FOR SUCCESS

- Keep admin password secure and unique
- Use email notifications for new orders
- Regularly backup your database
- Monitor server logs for errors
- Update dependencies monthly
- Test before deploying changes

Good luck! 🚀
