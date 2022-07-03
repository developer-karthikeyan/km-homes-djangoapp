from django.shortcuts import redirect
from .models import Contact
from django.contrib import messages
from listings.models import Listing
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from realestate.settings import EMAIL_HOST_USER # Importing Env variables from settings.py
from accounts.models import Profile
from django.contrib.auth.models import User

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_name=request.POST['listing_name']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        listing_id=request.POST['listing_id']
        realtor_email=request.POST['realtor_email']
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id,listing_id=listing_id)
            if has_contacted:
                messages.error(request,'You have already raised request for this listing')
                return redirect('listing',listing_id)
        contact_request=Contact(listing_name=listing_name,name=name,email=email,phone=phone,message=message,user_id=user_id,listing_id=listing_id)
        contact_request.save()
#Mail logic        
        email_subject, from_email, to_email = f'Request confirmation Mail for Property - {listing_name}', EMAIL_HOST_USER, email
        listing_details = Listing.objects.all().filter(pk=listing_id)        
        context={ 'listing_details' : listing_details, 'user_name' : request.user.first_name }
        html_content = render_to_string('contacts/confirmation_email.html', context) # will render & convert html into string
        text_content=strip_tags(html_content) # It will remove html tags from "html_content"
        msg = EmailMultiAlternatives(email_subject, text_content, from_email, [to_email]) # By default it will send text message. It can be read all kinds of user.
        msg.attach_alternative(html_content, "text/html") # additionally we are sending html content. Advanced users can view html format of mail message.
        msg.send()        
        email_subject, from_email, to_email = f'Request from our User - {name}', EMAIL_HOST_USER, realtor_email
        listing_details = Listing.objects.all().filter(pk=listing_id)        
        user_details=User.objects.get(pk=request.user.id)        
        context={ 
            'listing_details' : listing_details,
            'user_details' : user_details, 
            'email' : email, 
            'phone' : phone, 
            'message' : message }
        html_content = render_to_string('contacts/confirmation_email_to_realtor.html', context) # will render & convert html into string
        text_content=strip_tags(html_content) # It will remove html tags from "html_content"
        msg_to_realtor = EmailMultiAlternatives(email_subject, text_content, from_email, [to_email]) # By default it will send text message. It can be read all kinds of user.
        msg_to_realtor.attach_alternative(html_content, "text/html") # additionally we are sending html content. Advanced users can view html format of mail message.
        msg_to_realtor.send()
        messages.success(request,'Your request has been raised successfully. Our realtor will get back to u soon.')
        return redirect('listing',listing_id)