from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    listing_name=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.TextField(blank=True)
    listing_id=models.IntegerField()
    user_id=models.IntegerField()    
    contact_date=models.DateTimeField(default=datetime.now, blank=True)
    def __self__(self):
        return self.name