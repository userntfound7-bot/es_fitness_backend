from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class ClientManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Client(AbstractUser):
    username = None # Removes the default username field
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ClientManager()

    def __str__(self):
        return self.email

class TrainingBlock(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='workouts')
    day_label = models.CharField(max_length=50) 
    phase_focus = models.TextField(blank=True) 
    pdf_url = models.URLField(blank=True, null=True) 
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.client.email} - {self.day_label}"

class NutritionProtocol(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='meals')
    meal_timing = models.CharField(max_length=50) 
    target_macros = models.CharField(max_length=100) 
    food_sources = models.TextField(blank=True) 
    is_logged = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client.email} - {self.meal_timing}"