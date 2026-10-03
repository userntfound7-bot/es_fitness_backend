from rest_framework import viewsets
from .models import Client, TrainingBlock, NutritionProtocol
from .serializers import ClientSerializer, TrainingBlockSerializer, NutritionProtocolSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class TrainingBlockViewSet(viewsets.ModelViewSet):
    queryset = TrainingBlock.objects.all()
    serializer_class = TrainingBlockSerializer

class NutritionProtocolViewSet(viewsets.ModelViewSet):
    queryset = NutritionProtocol.objects.all()
    serializer_class = NutritionProtocolSerializer