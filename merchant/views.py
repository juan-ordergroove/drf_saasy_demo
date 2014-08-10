from rest_framework import viewsets
from models import Merchant
from serializers import MerchantSerializer


class MerchantViewSet(viewsets.ModelViewSet):
    """Simple merchant model viewset"""
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
