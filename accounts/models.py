from django.db import models
from django.utils import timezone


# Create your models here.
class IncomeAccount(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
