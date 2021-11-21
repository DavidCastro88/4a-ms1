from django.db import models
from .user import User
from .tourist_package import TouristPackage
from datetime import datetime,date

class ShoppingHistory(models.Model):
    Id_Purchase = models.AutoField(primary_key=True, null=False)
    Id_user =models.ForeignKey(User,on_delete=models.CASCADE)
    Id_tourist_package = models.ForeignKey(TouristPackage,on_delete=models.CASCADE)
    Amount_package= models.IntegerField(null=False, blank=False)
    Total_value= models.FloatField(null=False, blank=False)  
    Status = models.CharField(max_length=50, null=False, blank=False) 
    Shopping_Date = models.DateTimeField(auto_now_add=True)

   