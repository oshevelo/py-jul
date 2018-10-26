from django.db import models
from apps_generic.whodidit.models import WhoDidIt


class CatalogItem(WhoDidIt):
    name = models.CharField(max_length=200)

    description = models.TextField(
        verbose_name="Description",
        null=True, blank=True
    )
    index = models.IntegerField(
        verbose_name="index",
        default=0
    )


    perent = models.ForeignKey(
        verbose_name="perent",
        to='self', null=True, blank=True
    )

    def __str__(self):
        return '{} {}'.format(self.id, self.name)


class Product(WhoDidIt):

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
        verbose_name="Price",
        default=0   
    )

    status = models.CharField(
        verbose_name="Status",
        choices=STATUS_CHOICES, 
        max_length=40, default=Status.selling
    )

    catalog = models.ForeignKey(
        verbose_name="catalog ",
        to=CatalogItem, null=True, blank=True
    )

    def __str__(self):
        return '{} {}'.format(self.id, self.name)



