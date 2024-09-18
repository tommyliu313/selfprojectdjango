from django.db import models
from warehouse.choices import district_choices
# Create your models here.

class Warehouse(models.Model):
    title = models.CharField(max_length=50)
    region = models.CharField()
    district = models.CharField(max_length=50, choices=district_choices.items())
    floor = models.IntegerField()
    room = models.CharField()
    description = models.TextField()
    phone = models.CharField()
    main_img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    img1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    img2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    threemonrent = models.DecimalField(decimal_places=2, max_digits=5)
    sixmonrent = models.DecimalField(decimal_places=2, max_digits=5)
    ninemonrent = models.DecimalField(decimal_places=2, max_digits=5)
    is_listed = models.BooleanField()
    