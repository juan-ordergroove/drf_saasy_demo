"""Tiny client custom serializer"""
import random
from product.serializers import ProductSerializer as CoreProductSerializer


class ProductSerializer(CoreProductSerializer):
    """Tiny client custom serializer class"""

    def to_native(self, obj):
        nat = super(ProductSerializer, self).to_native(obj)
        price = nat.get('price')
        if price:
            discount_percent = random.random()
            discount_amount = float(price) * discount_percent
            sale_price = float(price) - discount_amount

            nat['discount_percent'] = '{:.2f}'.format(discount_percent * 100)
            nat['discount_amount'] = '{:.2f}'.format(discount_amount)
            nat['sale_price'] = '{:.2f}'.format(sale_price)
        return nat
