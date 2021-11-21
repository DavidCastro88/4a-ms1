from authshoppingapp.models.shopping_history import ShoppingHistory
from authshoppingapp.serializers.shopping_historySerializer import ShoppingHistorySerializer
from rest_framework import generics

class ShoppingHistoryListCreateView(generics.ListCreateAPIView):
    queryset = ShoppingHistory.objects.all()
    serializer_class = ShoppingHistorySerializer

class ShoppingHistoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingHistory.objects.all()
    serializer_class = ShoppingHistorySerializer

class UserHistory(generics.ListAPIView):
    serializer_class = ShoppingHistorySerializer
    def get_queryset(self):
        queryset = ShoppingHistory.objects.filter(Id_user= self.kwargs["pk"])
        return queryset
    
