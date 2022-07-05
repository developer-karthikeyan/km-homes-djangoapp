from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtor.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices 

from django.shortcuts import redirect, render
from django.contrib import messages
from listings.models import Listing
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from realestate.settings import EMAIL_HOST_USER, EMAIL_SEND_TO_EMAIL # Importing Env variables from settings.py
from .forms import ContactForm
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError
from django.http import HttpResponse

# Create your views here.
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'state_choices':state_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors=Realtor.objects.order_by('hire_date')
    mvp_realtor=Realtor.objects.all().filter(is_mvp=True)[:1]
    context={
        'realtors':realtors,
        'mvp_realtor':mvp_realtor
    }
    return render(request, 'pages/about.html', context)

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():	
            first_name=form.cleaned_data['first_name'] #cleaned_data dict is only have valid data. errors dict contain invalid data.
            last_name=form.cleaned_data['last_name'] 
            email=form.cleaned_data['email'] 
            phone=form.cleaned_data['phone']
            message=form.cleaned_data['message'] 		
            context = {
            'first_name' : first_name,
            'last_name' : last_name, 
            'email' : email, 
            'phone' : phone, 
            'message' : message,
            }	

            try:
                email_subject, from_email, to_email = "KM Homes website Inquiry", EMAIL_HOST_USER, EMAIL_SEND_TO_EMAIL            
                html_content = render_to_string('pages/contact_us_email.html', context) # will render & convert html into string
                text_content=strip_tags(html_content) # It will remove html tags from "html_content"
                msg = EmailMultiAlternatives(email_subject, text_content, from_email, [to_email]) # By default it will send text message. It can be read all kinds of user.
                msg.attach_alternative(html_content, "text/html") # additionally we are sending html content. Advanced users can view html format of mail message.
                msg.send()			
                messages.success(request,'Your Inquiry is submitted successfully. Our team will contact you soon.')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')            
            return redirect ("index")      
        else:
            form = ContactForm(request.POST) #It will get details form errors dict & show it in respective fields.
            return render(request, "pages/contact_us.html", {'form': form})
    form = ContactForm() # Get request empty form 
    return render(request, "pages/contact_us.html", {'form': form})