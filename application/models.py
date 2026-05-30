from django.db import models

class Employee(models.Model):
    DEPARTMENT_CHOICES = [
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('Finance', 'Finance'),
        ('Operations', 'Operations'),
        ('Sales', 'Sales'),
        ('Marketing', 'Marketing'),
    ]
    
    employee_name = models.CharField(max_length=100)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.employee_name


class Project(models.Model):
    STATUS_CHOICES = [
        ('Live', 'Live'),
        ('Not Live', 'Not Live'),
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('On Hold', 'On Hold'),
        ('Completed', 'Completed'),
    ]
    
    project_name = models.CharField(max_length=200)
    project_domain = models.CharField(max_length=100)
    domain_expiry_date = models.DateField(null=True, blank=True)
    domain_url = models.TextField(blank=True)
    project_amount = models.DecimalField(max_digits=12, decimal_places=2)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    @property
    def balance_amount(self):
        return self.total_amount - self.paid_amount
    
    def __str__(self):
        return self.project_name
