from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from listings.choices import state_list_for_admin_page

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default_profile_pic.jpg", upload_to="profile_pic")
    city=models.CharField(max_length=50, blank=True)
    state=models.CharField(max_length=50, choices=state_list_for_admin_page, blank=True) #choices should only be tuples
    phone=models.CharField(max_length=20, blank=True)

    def __self__(self):
        return f'{self.user} Profile'

    # def save(self, *args, **kwargs): #we must add this to allow extra arguments esle while Register & Login it will throw error.
    #     super(Profile, self).save(*args, **kwargs) #It first saves all 3 given parameters in Profile page. Then it go for resizing uploaded image based on its pixel.
    #     img=Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size=(300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

