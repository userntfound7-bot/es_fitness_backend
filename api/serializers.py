from rest_framework import serializers
from .models import Client, TrainingBlock, NutritionProtocol

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class TrainingBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingBlock
        fields = '__all__'

class NutritionProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionProtocol
        fields = '__all__'