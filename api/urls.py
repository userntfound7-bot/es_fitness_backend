from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, TrainingBlockViewSet, NutritionProtocolViewSet

# The router automatically generates the RESTful URL patterns
router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'training-blocks', TrainingBlockViewSet)
router.register(r'nutrition-protocols', NutritionProtocolViewSet)

urlpatterns = [
    path('', include(router.urls)),
]