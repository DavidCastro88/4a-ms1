from authshoppingapp.models.tourist_package import TouristPackage
from rest_framework import serializers
class TouristPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristPackage
        fields = ["Destination_place","Hotel","Days_stay","Nights_stay","Feeding","Guides","Price_Person"]