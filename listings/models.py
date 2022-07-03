from django.db import models
from datetime import datetime
from realtor.models import Realtor
from .choices import state_list_for_admin_page, bedroom_list_for_admin_page

# Create your models here.
class Listing(models.Model):
    realtor=models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50, choices=state_list_for_admin_page) #choices should only be tuples
    zipcode=models.CharField(max_length=10)
    description=models.TextField(blank=True)
    price=models.IntegerField()
    bedrooms=models.IntegerField(choices=bedroom_list_for_admin_page)
    bathrooms=models.DecimalField(max_digits=2,decimal_places=1)
    garage=models.IntegerField(default=0)
    sqft=models.IntegerField()
    lot_size=models.DecimalField(max_digits=4,decimal_places=1)
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    photo_main=models.ImageField(upload_to="photos/%y/%m/%d/")
    photo_1=models.ImageField(upload_to="photos/%y/%m/%d/", blank=True)
    photo_2=models.ImageField(upload_to="photos/%y/%m/%d/", blank=True)
    photo_3=models.ImageField(upload_to="photos/%y/%m/%d/", blank=True)
    photo_4=models.ImageField(upload_to="photos/%y/%m/%d/", blank=True)
    photo_5=models.ImageField(upload_to="photos/%y/%m/%d/", blank=True)
    photo_6=models.ImageField(upload_to="photos/%y/%m/%d/", blank=True)
    def __str__(self):
        return (self.title)