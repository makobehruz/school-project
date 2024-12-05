from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Post(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    email = models.EmailField(max_length=100)
