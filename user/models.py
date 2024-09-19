from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    creation_date = models.DateTimeField()
    email = models.EmailField(max_length=254)
    phone = models.CharField()
    is_active = models.BooleanField(default=True)