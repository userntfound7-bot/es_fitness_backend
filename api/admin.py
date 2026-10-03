from django.contrib import admin
from .models import Client, TrainingBlock, NutritionProtocol

admin.site.register(Client)
admin.site.register(TrainingBlock)
admin.site.register(NutritionProtocol)