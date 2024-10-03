from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField()
    last_name = models.CharField()
    creation_date = models.DateTimeField()
    email = models.EmailField(max_length=254)
    phone = models.CharField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username