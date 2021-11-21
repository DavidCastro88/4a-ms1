from authshoppingapp.models.tourist_package import TouristPackage
from authshoppingapp.serializers.tourist_packageSerializer import TouristPackageSerializer
from rest_framework import generics

class TouristPackageListCreateView(generics.ListCreateAPIView):
    queryset = TouristPackage.objects.all()
    serializer_class = TouristPackageSerializer

class TouristPackageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TouristPackage.objects.all()
    serializer_class = TouristPackageSerializer