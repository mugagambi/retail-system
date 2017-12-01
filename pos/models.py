from django.db import models


# Create your models here.
class Receipt(models.Model):
    receipt_no = models.CharField(max_length=10, unique=True)
    receipt_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    date = models.DateTimeField(auto_now_add=True)


class ReceiptItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    receipt = models.ForeignKey(Receipt)

    def __str__(self):
        return self.name

    def save_base(self, raw=False, force_insert=False,
                  force_update=False, using=None, update_fields=None):
        self.receipt.receipt_total += self.total_amount
        self.receipt.save()
        super(ReceiptItem, self).save_base(raw=False, force_insert=False,
                                           force_update=False, using=None, update_fields=None)

    @property
    def total_amount(self):
        return self.quantity * self.unit_price
