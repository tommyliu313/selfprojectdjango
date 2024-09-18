from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    creation_date = models.DateTimeField()
    main_img = models.ImageField()
    email = models.EmailField(max_length=254)
    phone = models.CharField()
    is_active = models.BooleanField(default=True)