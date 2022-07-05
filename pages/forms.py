from django import forms
from django.core.validators import MinLengthValidator, RegexValidator, MaxLengthValidator
# Create your forms here.

class ContactForm(forms.Form):
    first_name = forms.CharField(
        widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First Name'})), 
        validators=[MinLengthValidator(3),RegexValidator(r'^[a-zA-Z\s]+$',message='Please enter valid First name (Numbers & Special characters are not acceptable)')],
        max_length=32)
    last_name=forms.CharField(
        widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name'})), 
        validators=[RegexValidator(r'^[a-zA-Z\s]+$',message='Please enter valid Last name (Numbers & Special characters are not acceptable)')],
        max_length=32)
    email=forms.EmailField(
        widget=(forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email address'})), 
        max_length=64, 
        validators=[MinLengthValidator(10),RegexValidator(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',message='Please enter valid Email address')])    
    message = forms.CharField(    
        widget=(forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your Message'})), 
        max_length = 2000)
    phone=forms.CharField(
         widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Phone number'})), 
        validators=[MaxLengthValidator(10),RegexValidator(r'[0-9]{10}',message='Please enter valid number (Aphabets & Special characters are not acceptable)')])