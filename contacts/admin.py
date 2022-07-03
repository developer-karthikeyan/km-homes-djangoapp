from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','email','listing_name','contact_date')
    list_display_links=('id','name')
    list_per_page=10
    search_fields=('name','email','listing_name')
admin.site.register(Contact, ContactAdmin)