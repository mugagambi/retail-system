from django.db import models
from accounts.models import IncomeAccount


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    total_units = models.IntegerField()
    remaining_units = models.IntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    account = models.ForeignKey(IncomeAccount)

    def __str__(self):
        return self.name
