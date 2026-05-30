# Django Admin Dashboard

A professional, feature-rich admin dashboard system built with Django for managing Employees and Projects with complete CRUD operations, authentication, and an attractive modern UI.

## Features

✨ **Authentication & Security**
- User registration and login system
- Password hashing and validation
- Admin access control with Django admin panel
- Session management

👥 **Employee Management**
- Complete CRUD operations (Create, Read, Update, Delete)
- Columns: Employee Name, Department, Designation, Phone Number, Salary
- Search and filter by name, designation, or department
- Serial number for each record
- Professional table view with actions

📊 **Project Management**
- Complete CRUD operations (Create, Read, Update, Delete)
- Columns: Project Name, Domain, Project Amount, Total Amount, Paid Amount
- Auto-calculated Balance Amount (Total Amount - Paid Amount)
- Status tracking (Active, Inactive, On Hold, Completed)
- Search and filter by project name, domain, or status
- Serial number for each record
- Payment progress visualization

🎨 **Professional UI**
- Modern, responsive design
- Sidebar navigation with active states
- Dashboard with statistics and quick actions
- Bootstrap 5 integration
- Font Awesome icons
- Mobile-friendly responsive layout
- Smooth animations and transitions
- Color-coded badges and status indicators

## Project Structure

```
web/
├── manage.py
├── db.sqlite3
├── application/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py              # Admin site configuration
│   ├── apps.py
│   ├── forms.py              # Django forms for models
│   ├── models.py             # Employee and Project models
│   ├── tests.py
│   ├── urls.py               # Application URL routes
│   └── views.py              # View functions for all operations
├── web/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py
├── templates/
│   ├── base.html             # Base template with sidebar
│   ├── index.html            # Home page
│   ├── dashboard.html        # Main dashboard
│   ├── registration/
│   │   ├── login.html        # Login page
│   │   └── register.html     # Registration page
│   ├── employee/
│   │   ├── list.html         # Employee list with search/filter
│   │   ├── form.html         # Employee create/update form
│   │   └── detail.html       # Employee detail view
│   └── project/
│       ├── list.html         # Project list with search/filter
│       ├── form.html         # Project create/update form
│       └── detail.html       # Project detail view
└── static/
    ├── css/
    │   └── style.css         # Main stylesheet
    └── js/
        └── main.js           # JavaScript functionality
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Django 6.0+

### Step 1: Install Dependencies

```bash
pip install django
```

### Step 2: Navigate to Project Directory

```bash
cd d:\spitel\web
```

### Step 3: Run Migrations

```bash
python manage.py migrate
```

### Step 4: Create Superuser Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

OR use pre-configured credentials:
- Username: `admin`
- Password: `admin123`

To set this password:
```bash
python manage.py shell -c "from django.contrib.auth.models import User; user = User.objects.get(username='admin'); user.set_password('admin123'); user.save()"
```

### Step 5: Run Development Server

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

## Usage

### Access Points

1. **Home Page**: `http://127.0.0.1:8000/`
2. **Login**: `http://127.0.0.1:8000/app/login/`
3. **Register**: `http://127.0.0.1:8000/app/register/`
4. **Dashboard**: `http://127.0.0.1:8000/app/dashboard/`
5. **Admin Panel**: `http://127.0.0.1:8000/admin/`

### Employee Management

**List View**: `/app/employees/`
- View all employees with serial numbers
- Search by employee name or designation
- Filter by department
- CRUD operations with action buttons

**Add Employee**: `/app/employees/create/`
- Fill in form with required information
- Department dropdown selection
- Form validation

**Edit Employee**: `/app/employees/<id>/edit/`
- Update any employee information
- Automatic save on submit

**Delete Employee**: Via list view delete button
- Confirmation dialog before deletion

### Project Management

**List View**: `/app/projects/`
- View all projects with auto-calculated balance
- Search by project name or domain
- Filter by status (Active, Inactive, On Hold, Completed)
- Color-coded status badges
- CRUD operations with action buttons

**Add Project**: `/app/projects/create/`
- Fill in project details
- Balance automatically calculated
- Real-time balance preview

**Edit Project**: `/app/projects/<id>/edit/`
- Update project information
- Balance auto-calculated
- Update payment status

**Delete Project**: Via list view delete button
- Confirmation dialog before deletion

## Models

### Employee Model

| Field | Type | Description |
|-------|------|-------------|
| employee_name | CharField(100) | Name of the employee |
| department | CharField(50) | Department (HR, IT, Finance, Operations, Sales, Marketing) |
| designation | CharField(100) | Job designation |
| phone_number | CharField(15) | Contact phone number |
| salary | DecimalField | Monthly/Annual salary |
| created_at | DateTimeField | Creation timestamp |
| updated_at | DateTimeField | Last update timestamp |

### Project Model

| Field | Type | Description |
|-------|------|-------------|
| project_name | CharField(200) | Name of the project |
| project_domain | CharField(100) | Project domain/category |
| project_amount | DecimalField | Base project amount |
| total_amount | DecimalField | Total project cost |
| paid_amount | DecimalField | Amount already paid |
| balance_amount | Computed Property | total_amount - paid_amount (Auto-calculated) |
| status | CharField(20) | Project status (Active, Inactive, On Hold, Completed) |
| created_at | DateTimeField | Creation timestamp |
| updated_at | DateTimeField | Last update timestamp |

## Features in Detail

### Authentication
- User registration with email validation
- Secure login with session management
- Password hashing using Django's authentication system
- Login required for all protected views
- Automatic redirect to login for unauthorized access

### Search & Filter
- Real-time search functionality
- Filter by department (employees) or status (projects)
- Combined search and filter operations
- Case-insensitive search

### CRUD Operations
- **Create**: Add new records with validated forms
- **Read**: View records in list and detail views
- **Update**: Edit existing records with pre-filled forms
- **Delete**: Remove records with confirmation dialog

### Dashboard Features
- Overview statistics (total employees, projects, active projects)
- Quick action buttons for adding new records
- Links to view all records
- Visual stat cards with icons

### Data Validation
- Required field validation
- Email validation on registration
- Phone number format validation
- Decimal/numeric field validation
- Confirmation dialogs for destructive actions

## Styling & Design

### Color Scheme
- Primary: #2c3e50 (Dark blue-gray)
- Secondary: #3498db (Bright blue)
- Success: #27ae60 (Green)
- Danger: #e74c3c (Red)
- Warning: #f39c12 (Orange)

### Responsive Design
- Mobile-first approach
- Breakpoints for tablets and phones
- Collapsible sidebar on mobile
- Touch-friendly buttons and controls

### UI Components
- Bootstrap 5 framework
- Font Awesome icons
- Custom CSS for animations
- Smooth transitions and hover effects
- Professional card layouts

## Database

### SQLite (Default)
- File-based database: `db.sqlite3`
- Suitable for development and small deployments
- No additional setup required

### Migration System
- Automatic schema management
- Version control for database changes
- Reversible migrations

## Security Features

- CSRF token protection on all forms
- Session-based authentication
- Password hashing with Django's password validators
- SQL injection protection via ORM
- User permission checks on all views
- Admin panel with Django's built-in security

## Admin Panel

Access Django admin at: `/admin/`

### Features
- Full CRUD management of employees and projects
- Search and filtering
- List display customization
- Admin actions
- User and permission management

## Troubleshooting

### Port Already in Use
If port 8000 is already in use:
```bash
python manage.py runserver 8080
```

### Static Files Not Loading
Collect static files:
```bash
python manage.py collectstatic
```

### Database Issues
Reset database (warning: data loss):
```bash
python manage.py flush
python manage.py migrate
```

### Template Not Found
Ensure `settings.py` has correct `TEMPLATES['DIRS']` path pointing to templates folder.

## Performance Tips

1. Use Django admin for bulk operations
2. Implement pagination for large datasets (future enhancement)
3. Add database indexes on frequently searched fields
4. Use caching for dashboard statistics
5. Optimize static files delivery

## Future Enhancements

- [ ] Pagination for large datasets
- [ ] Export to CSV/Excel functionality
- [ ] Advanced reporting and analytics
- [ ] Email notifications
- [ ] File uploads for documents
- [ ] Audit logging
- [ ] Advanced filtering and sorting
- [ ] Dashboard charts and graphs
- [ ] API endpoints (REST)
- [ ] User roles and permissions
- [ ] Two-factor authentication
- [ ] Dark mode

## License

This project is free to use for educational and commercial purposes.

## Support

For issues or questions, please review the code comments or Django documentation at https://docs.djangoproject.com/

---

**Created**: May 30, 2026
**Version**: 1.0
**Status**: Production Ready
