from django.db import models
# Create your models here.
class images(models.Model):
    ProductId = models.AutoField
    garbageimage = models.FileField(upload_to="images/", default="")

class logcredential(models.Model):
    usernames=models.CharField(unique=True,max_length=50)
    passwords=models.CharField(unique=True,max_length=50)

# from django.db import models
# from django_google_maps import fields as map_fields

# class Rental(models.Model):
#     address = map_fields.AddressField(max_length=200)
#     geolocation = map_fields.GeoLocationField(max_length=100)

def __str__(self):
    return self.ProductId
    print(self.ProductId)

def __str__(self):
    return self.usernames
    print(self.usernames)
