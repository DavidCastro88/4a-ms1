from django.db import models
from datetime import datetime,date

class TouristPackage(models.Model):
    Id_tourist_package = models.AutoField(primary_key=True, null=False)
    Destination_place=models.CharField(max_length=50, null=False)
    Hotel=models.CharField(max_length=50, null=False)
    Days_stay = models.IntegerField(null=False, blank=False) 
    Nights_stay = models.IntegerField(null=False, blank=False)
    Feeding = models.BooleanField(default=True)
    Guides= models.BooleanField(default=True)
    Price_Person= models.IntegerField(null=False, blank=False) 
    def __str__(self):
        return self.Id_tourist_package