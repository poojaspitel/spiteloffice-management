from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employee, Project


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name', 'department', 'designation', 'phone_number', 'salary']
        widgets = {
            'employee_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter employee name'
            }),
            'department': forms.Select(attrs={
                'class': 'form-control'
            }),
            'designation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter designation'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number',
                'type': 'tel'
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter salary',
                'step': '0.01'
            }),
        }


class ProjectForm(forms.ModelForm):
    status = forms.ChoiceField(
        choices=[('Live', 'Live'), ('Not Live', 'Not Live')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Project
        fields = ['project_name', 'project_domain', 'domain_expiry_date', 'domain_url', 'project_amount', 'total_amount', 'paid_amount', 'status']
        widgets = {
            'project_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project name'
            }),
            'project_domain': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter domain name',
                'rows': 2
            }),
            'domain_expiry_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'domain_url': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter domain URL',
                'rows': 2
            }),
            'project_amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project amount',
                'step': '0.01'
            }),
            'total_amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter total amount',
                'step': '0.01'
            }),
            'paid_amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter paid amount',
                'step': '0.01'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
