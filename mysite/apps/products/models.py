from django.db import models


class Product(models.Model):

    class Status:
        selling = 'selling'
        no_stock = 'no_stock'
        no_prod = 'no_prod'

    STATUS_CHOICES = (
        (Status.selling, "On sale"),
        (Status.no_stock, "No stock"),
        (Status.no_prod, "Production process ended")
    )

    name = models.CharField(max_length=200)
    description = models.TextField(
        verbose_name="Description",
        null=True, blank=True
    )

    price = models.FloatField(
        verbose_name="Price"
    )

    status = models.CharField(
        verbose_name="Status",
        choices=STATUS_CHOICES
    )

    def __str__(self):
        return '{} {}'.format(self.id, self.name)
