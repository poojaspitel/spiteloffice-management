from django.contrib import admin
from .models import Employee, Project


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'department', 'designation', 'phone_number', 'salary', 'created_at')
    search_fields = ('employee_name', 'designation', 'phone_number')
    list_filter = ('department', 'created_at')
    ordering = ('-created_at',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_domain', 'total_amount', 'paid_amount', 'balance_amount', 'status', 'created_at')
    search_fields = ('project_name', 'project_domain')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)

