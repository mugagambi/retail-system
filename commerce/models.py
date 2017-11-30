from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)
