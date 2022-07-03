from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','price','is_published','list_date','realtor')
    list_display_links=('id','title')
    list_per_page=10
    list_editable=('is_published',)
    search_fields=('title','price','description','address','city','state')
    ordering=('id','-list_date')
    list_filter=('realtor',)
    fields=['title',('address','city'),('state','zipcode'),'description','price',('bedrooms','bathrooms'),('garage','sqft'),'lot_size','is_published','list_date','photo_main',('photo_1','photo_2','photo_3'),('photo_4','photo_5','photo_6'),'realtor']
    # Register your models here.
admin.site.register(Listing, ListingAdmin)