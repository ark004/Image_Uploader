from django.db import models

# Create your models here.
class image(models.Model):
    photo = models.ImageField(upload_to="picture")
    date = models.DateField(auto_now_add=True)
    


  