from django import forms
from django.core.validators import MinLengthValidator, RegexValidator, MaxLengthValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile 
# from django.contrib.auth.forms import PasswordChangeForm

class UserRegistartionForm(UserCreationForm):
    username = forms.CharField(
        widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Username'})),
        validators=[MinLengthValidator(3),RegexValidator(r'^[a-zA-Z0-9_.]+$',message='Please enter valid Username (special characters : only Dot ( . ) and Underscore ( _ ) alone acceptable)')]
        )
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
    password1=forms.CharField(
        widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Please enter strong Password'})))
    password2=forms.CharField(
        label="Confirm Password",
        widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-type Password Again'})))
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username','email','password1','password2']


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First Name'})), 
        validators=[MinLengthValidator(3),RegexValidator(r'^[a-zA-Z\s]+$',message='Please enter valid First name (Numbers & Special characters are not acceptable)')],
        max_length=32)
    last_name=forms.CharField(
        widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name'})), 
        validators=[RegexValidator(r'^[a-zA-Z\s]+$',message='Please enter valid Last name (Numbers & Special characters are not acceptable)')],
        max_length=32)
    class Meta:        
        model = User
        fields = ('first_name', 'last_name')
        
class ProfileUpdateForm(forms.ModelForm):
    city=forms.CharField(validators=[MinLengthValidator(3),RegexValidator(r'^[a-zA-Z\s,]+$',message='Please enter valid City name (Numbers & Special characters are not acceptable)')])
    phone=forms.CharField(validators=[MaxLengthValidator(10),RegexValidator(r'[0-9]{10}',message='Please enter valid number (Aphabets & Special characters are not acceptable)')])
    class Meta:
        model = Profile
        fields = ('image','city','state','phone')
        widgets={
            'city': forms.TextInput(attrs={'placeholder':'Enter your city name'}),
            'phone': forms.TextInput(attrs={'placeholder':'Enter your 10 digit phone number'}),
        }