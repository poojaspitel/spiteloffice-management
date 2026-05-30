from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.db.models import Q
from .models import Employee, Project
from .forms import UserRegistrationForm, EmployeeForm, ProjectForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    employees_count = Employee.objects.count()
    projects_count = Project.objects.count()
    active_projects = Project.objects.filter(status='Active').count()
    
    context = {
        'employees_count': employees_count,
        'projects_count': projects_count,
        'active_projects': active_projects,
    }
    return render(request, 'dashboard.html', context)


# ===== EMPLOYEE VIEWS =====

@login_required
def employee_list(request):
    search = request.GET.get('search', '')
    department = request.GET.get('department', '')
    
    employees = Employee.objects.all()
    
    if search:
        employees = employees.filter(
            Q(employee_name__icontains=search) | Q(designation__icontains=search)
        )
    
    if department:
        employees = employees.filter(department=department)
    
    departments = Employee.DEPARTMENT_CHOICES
    
    context = {
        'employees': employees,
        'departments': departments,
        'search': search,
        'department': department,
    }
    return render(request, 'employee/list.html', context)


@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee created successfully!')
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    
    context = {'form': form, 'title': 'Add Employee'}
    return render(request, 'employee/form.html', context)


@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {'employee': employee}
    return render(request, 'employee/detail.html', context)


@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully!')
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    
    context = {'form': form, 'title': 'Edit Employee', 'employee': employee}
    return render(request, 'employee/form.html', context)


@login_required
@require_http_methods(["POST"])
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    messages.success(request, 'Employee deleted successfully!')
    return redirect('employee_list')


# ===== PROJECT VIEWS =====

@login_required
def project_list(request):
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')
    
    projects = Project.objects.all()
    
    if search:
        projects = projects.filter(
            Q(project_name__icontains=search) | Q(project_domain__icontains=search)
        )
    
    if status:
        projects = projects.filter(status=status)
    
    status_choices = Project.STATUS_CHOICES
    
    context = {
        'projects': projects,
        'status_choices': status_choices,
        'search': search,
        'status': status,
    }
    return render(request, 'project/list.html', context)


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project created successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm()
    
    context = {'form': form, 'title': 'Add Project'}
    return render(request, 'project/form.html', context)


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {'project': project}
    return render(request, 'project/detail.html', context)


@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    
    context = {'form': form, 'title': 'Edit Project', 'project': project}
    return render(request, 'project/form.html', context)


@login_required
@require_http_methods(["POST"])
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    messages.success(request, 'Project deleted successfully!')
    return redirect('project_list')

