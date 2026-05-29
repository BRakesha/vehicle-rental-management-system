from django.db import models

# Create your models here.

class CarModel(models.Model):
    name=models.CharField()
    brand=models.CharField()
    fuel_type=models.CharField()
    price_per_day=models.IntegerField()
    seats=models.IntegerField(default=4)
    transmission=models.CharField()
    image=models.CharField(null=True)
    availability=models.BooleanField(default=True)