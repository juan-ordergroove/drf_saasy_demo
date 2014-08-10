"""Product app related models"""
from django.db import models


class Product(models.Model):
    """Product data model"""
    merchant = models.ForeignKey('merchant.Merchant')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'{} - {} - ${:2f}'.format(self.merchant.name,
                                          self.name,
                                          self.price
                                          )
