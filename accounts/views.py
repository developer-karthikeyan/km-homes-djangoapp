from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from realestate.settings import EMAIL_HOST_USER, domain, site_name, protocol
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django import template
from .models import Profile
from .forms import UpdateUserForm, ProfileUpdateForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from .forms import UserRegistartionForm

def register(request):
    if request.method == 'POST':
        form = UserRegistartionForm(request.POST)        
        if form.is_valid():
            form.save()        
            messages.success(request, "Registration done successfully")
            return redirect('dashboard')
    else:
        form = UserRegistartionForm()
    return render(request, 'accounts/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'You are logged in successfully.')
            if 'next' in request.POST: #If 'next' value is present in POST request. Then it will get redirect like eg: return redirect('/listings/5')
                return redirect(request.POST.get('next')) 
            else:             
                return redirect('dashboard')
        else:
            context = {
                'username' : username,
                'password' : password
            }   
            messages.error(request,'Username or Password is incorrect.')
            # return redirect('login')
            return render(request, 'accounts/login.html', context)
    else:       
        return render(request, 'accounts/login.html')
    
@login_required(login_url="/accounts/login/") #It will prevent access dashboard page without login.
def dashboard(request):
    if request.user.is_authenticated:
        contact_details = Contact.objects.all().filter(user_id=request.user.id).order_by('-contact_date')
        context={'contact_details' : contact_details}
        return render(request, 'accounts/dashboard.html', context)        

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"You are logged out successfully.")
        return redirect('index')

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					context1={
                        'email':user.email,
                        'domain': domain,
                        'site_name': site_name,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user),
                        'protocol': protocol,
                    }
					text_email_content = template.loader.get_template('password/password_reset_email.txt').render(context1)
					html_email_content = template.loader.get_template('password/password_reset_email.html').render(context1)
					try:						
						msg = EmailMultiAlternatives(subject, text_email_content, EMAIL_HOST_USER, [user.email])
						msg.attach_alternative(html_email_content, "text/html")
						msg.send()
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("password_reset_done")
	password_reset_form = PasswordResetForm()
	return render(request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})

@login_required(login_url="/accounts/login/")
def password_change_request(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request,"Password changed successfully")
            return redirect ("profile")
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, template_name="password/password_change.html", context={"form":form})

# @login_required(login_url="/accounts/login/")
# class UserdefinedPasswordChangeView(PasswordChangeView):
#     form = PasswordChangeForm
#     success_url=reverse_lazy('profile')

@login_required(login_url="/accounts/login/")
def profile(request):
    if request.method == 'POST':
        user_obj=User.objects.get(pk=request.user.id)
        profile_obj=Profile.objects.get(pk=request.user.profile.id)
        u_form = UpdateUserForm(request.POST, instance=user_obj) #assigning POSTed data to UpdateUserForm class obj.
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile_obj) #assigning POSTed data to ProfileUpdateForm class obj.
        if u_form.is_valid() and p_form.is_valid(): #It will check for valid data then only It will save.
            u_form.save()
            p_form.save()
            messages.success(request,'Your Profile updated successfully !')
            return redirect('profile')
        else:
            context = {
            'u_form' : u_form,
            'p_form' : p_form
            }
            return render(request, 'accounts/profile.html', context)  
    else:            
        user_obj=User.objects.get(pk=request.user.id)
        profile_obj=Profile.objects.get(pk=request.user.profile.id)
        u_form = UpdateUserForm(instance=user_obj)
        p_form = ProfileUpdateForm(instance=profile_obj)
        context = {
            'u_form' : u_form,
            'p_form' : p_form
        }
        return render(request, 'accounts/profile.html', context)    