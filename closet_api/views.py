from rest_framework import generics
from .serializers import ClothingSerializer
from .models import Clothing

class ClothingList(generics.ListCreateAPIView):
    queryset = Clothing.objects.all().order_by('id')
    serializer_class = ClothingSerializer

class ClothingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothing.objects.all().order_by('id')
    serializer_class = ClothingSerializer
