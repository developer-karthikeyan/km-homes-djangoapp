from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from .choices import bedroom_choices, price_choices, state_choices
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    listings_obj=Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator_obj=Paginator(listings_obj,3)
    page_num=request.GET.get('page')
    page_obj=paginator_obj.get_page(page_num)
    context={
        'listings': page_obj,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'state_choices':state_choices
    }
    return render(request, 'listings/listings.html', context)

@login_required(login_url="/accounts/login/")
def listing(request, listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)
    context ={
        'listing':listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    full_listing=Listing.objects.order_by('-list_date').filter(is_published=True)

    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            full_listing=full_listing.filter(description__icontains=keywords)
    
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            full_listing=full_listing.filter(city__iexact=city)

    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            full_listing=full_listing.filter(state__icontains=state)

    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            full_listing=full_listing.filter(bedrooms__lte=bedrooms).order_by('-bedrooms')

    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            full_listing=full_listing.filter(price__lte=price).order_by('-price')

    context={
        'listings': full_listing,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'state_choices':state_choices,
        'values':request.GET
    }
    return render(request, 'listings/search.html', context)