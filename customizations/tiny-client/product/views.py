# from rest_framework.response import Response
from product.views import ProductViewSet as CoreProductViewSet
from .serializers import ProductSerializer


class ProductViewSet(CoreProductViewSet):
    """This is tiny-clients custom ViewSet!!"""
    serializer_class = ProductSerializer
