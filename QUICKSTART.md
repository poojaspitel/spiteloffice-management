# Quick Start Guide

## 🚀 Get Started in 5 Steps

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Migrations
```bash
python manage.py migrate
```

### 3. Set Admin Password (Optional)
```bash
python manage.py shell -c "from django.contrib.auth.models import User; user = User.objects.get(username='admin'); user.set_password('admin123'); user.save()"
```

### 4. Start Server
```bash
python manage.py runserver
```

### 5. Access Application
- **Application**: http://127.0.0.1:8000/
- **Login**: http://127.0.0.1:8000/app/login/
- **Admin**: http://127.0.0.1:8000/admin/

---

## 📋 Default Credentials

**Admin Account**
- Username: `admin`
- Password: `admin123`

---

## 🎯 Quick Navigation

| Page | URL |
|------|-----|
| Home | `/` |
| Login | `/app/login/` |
| Register | `/app/register/` |
| Dashboard | `/app/dashboard/` |
| Employees | `/app/employees/` |
| Add Employee | `/app/employees/create/` |
| Projects | `/app/projects/` |
| Add Project | `/app/projects/create/` |
| Admin Panel | `/admin/` |

---

## ✨ Key Features

✅ **Employee Management**
- Add, Edit, Delete employees
- Search and filter by department
- View employee details
- Serial numbers for each record

✅ **Project Management**
- Add, Edit, Delete projects
- Auto-calculated balance amount
- Status tracking (Active/Inactive/On Hold/Completed)
- Search and filter by status
- Payment progress visualization
- Serial numbers for each record

✅ **Professional Dashboard**
- Statistics overview
- Quick action buttons
- Responsive design
- Beautiful sidebar navigation

✅ **Security**
- User authentication required
- Password hashing
- CSRF protection
- Secure session management

---

## 📦 Project Structure

```
web/
├── manage.py              # Django management script
├── db.sqlite3             # SQLite database
├── requirements.txt       # Python dependencies
├── README.md              # Full documentation
├── QUICKSTART.md          # This file
├── application/           # Main Django app
│   ├── models.py          # Employee and Project models
│   ├── views.py           # All view functions
│   ├── forms.py           # Django forms
│   ├── urls.py            # App URL patterns
│   ├── admin.py           # Admin customization
│   └── migrations/        # Database migrations
├── web/                   # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL config
│   ├── asgi.py
│   └── wsgi.py
├── templates/             # HTML templates
│   ├── base.html          # Base layout
│   ├── dashboard.html     # Dashboard page
│   ├── registration/      # Auth templates
│   ├── employee/          # Employee templates
│   └── project/           # Project templates
└── static/                # CSS and JavaScript
    ├── css/style.css      # Main stylesheet
    └── js/main.js         # JavaScript functions
```

---

## 🎨 Design Features

- **Modern UI** with Bootstrap 5
- **Responsive Design** for all devices
- **Color-coded Status** indicators
- **Smooth Animations** and transitions
- **Professional Icons** using Font Awesome
- **Dark Sidebar** with active state highlighting
- **Beautiful Cards** with hover effects
- **Mobile-friendly** navigation

---

## 🔧 Common Commands

### Create Admin User
```bash
python manage.py createsuperuser
```

### Run Migrations
```bash
python manage.py migrate
```

### Create Migrations
```bash
python manage.py makemigrations
```

### Run Tests
```bash
python manage.py test
```

### Collect Static Files
```bash
python manage.py collectstatic
```

### Enter Django Shell
```bash
python manage.py shell
```

### Reset Database (Warning: Data Loss!)
```bash
python manage.py flush
```

---

## 💡 Tips & Tricks

1. **Superuser Already Created**: The admin user is pre-created. Just set a password if needed.

2. **Auto-calculated Fields**: Balance amount for projects is automatically calculated as (Total Amount - Paid Amount).

3. **Search Features**: Use the search boxes to filter employees and projects in real-time.

4. **Responsive Design**: The dashboard works great on mobile, tablet, and desktop!

5. **Admin Panel**: Use `/admin/` for bulk operations and advanced management.

---

## ⚠️ Troubleshooting

**Issue**: Port 8000 already in use
```bash
python manage.py runserver 8080
```

**Issue**: Static files not loading
```bash
python manage.py collectstatic
```

**Issue**: Template errors
- Check that `TEMPLATES` setting in `settings.py` points to `templates/` directory

**Issue**: Database errors
```bash
python manage.py migrate --run-syncdb
```

---

## 📧 Form Fields

### Employee Form
- ✅ Employee Name (required)
- ✅ Department (dropdown: HR, IT, Finance, Operations, Sales, Marketing)
- ✅ Designation (required)
- ✅ Phone Number (required)
- ✅ Salary (required, decimal)

### Project Form
- ✅ Project Name (required)
- ✅ Project Domain (required)
- ✅ Project Amount (required, decimal)
- ✅ Total Amount (required, decimal)
- ✅ Paid Amount (required, decimal)
- ✅ Status (dropdown: Active, Inactive, On Hold, Completed)

---

## 🎓 Learning Resources

- Django Official Docs: https://docs.djangoproject.com/
- Bootstrap 5: https://getbootstrap.com/docs/5.0/
- Font Awesome: https://fontawesome.com/
- SQLite: https://www.sqlite.org/docs.html

---

**Happy Coding! 🚀**
