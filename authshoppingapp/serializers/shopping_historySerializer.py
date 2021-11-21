from authshoppingapp.models.shopping_history import ShoppingHistory
from rest_framework import serializers

class ShoppingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ShoppingHistory
        fields=["Id_user","Id_tourist_package","Amount_package","Total_value","Status"]
    """def to_representation(self, obj):
        
            representation obj to return 
        
        history = ShoppingHistory.objects.get(id=obj.Id_user)
        return {
                'Id_Purchase': history.Id_Purchase, 
                'Id_user': history.Id_user,
                'Id_tourist_package': history.Id_tourist_package,
                'Amount_package': history.Amount_package,
                'Total_value': history.Total_value,
                'Status': history.Status,
                'Shopping_Date': history.Shopping_Date,
                }"""