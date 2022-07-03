from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display=('id','name','phone','hire_date','is_mvp')
    list_display_links=('id','name')
    search_fields=('name',)
    ordering=('id',)
    list_per_page=10
    fields=['name','photo','description',('phone','email'),'is_mvp','hire_date']
# Register your models here.
admin.site.register(Realtor, RealtorAdmin)