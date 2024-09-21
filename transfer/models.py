from django.db import models
from user.models import User
from warehouse.models import Warehouse
# Create your models here.

class Transfer(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.DO_NOTHING)
    rent_date = models.DateTimeField()
    end_date = models.DateTimeField()
    rent_paid = models.FloatField()
    is_active = models.BooleanField(default=True)