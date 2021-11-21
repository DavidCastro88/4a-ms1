from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.shopping_history import ShoppingHistory
from .models.tourist_package import TouristPackage
admin.site.register(User)
admin.site.register(Account)
admin.site.register(ShoppingHistory)
admin.site.register(TouristPackage)
# Register your models here.
