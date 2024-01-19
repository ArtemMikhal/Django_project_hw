from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

from catalog.models import NULLABLE

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone_number = models.CharField(max_length=35, verbose_name ='телефон', **NULLABLE)
    country = models.CharField(max_length=100, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


