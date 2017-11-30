from django.db import models
from django.contrib.auth.models import User
from inventory.models import Item


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Order(models.Model):
    customer = models.ForeignKey(Customer)
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()
    processed = models.BooleanField(default=False)
    already_processed = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.already_processed:
            if self.processed:
                self.item.remaining_units -= self.quantity
                self.item.save()
                self.already_processed = True
        super(Order, self).save(force_insert=False, force_update=False, using=None,
                                update_fields=None)

    def __str__(self):
        return str(self.customer)
