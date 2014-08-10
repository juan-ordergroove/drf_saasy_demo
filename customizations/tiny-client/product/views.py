#from rest_framework.response import Response
from product.views import ProductViewSet as CoreProductViewSet


class ProductViewSet(CoreProductViewSet):
    """This is tiny-clients custom ViewSet!!"""
    pass
