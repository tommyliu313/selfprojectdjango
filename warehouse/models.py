from django.db import models

# Create your models here.

class Warehouse(models.Model):
    title = models.CharField(max_length=50)
    region = models.CharField()
    district = models.CharField()
    floor = models.IntegerField()
    room = models.CharField()
    description = models.TextField()
    phone = models.CharField()
    main_img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    img1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    img2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    threemonrent = models.DecimalField()
    sixmonrent = models.DecimalField()
    ninemonrent = models.DecimalField()
    is_listed = models.BooleanField()
    