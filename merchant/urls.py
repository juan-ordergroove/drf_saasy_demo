"""Merchant app related URLs"""
from django.conf.urls import patterns, url, include
from rest_framework import routers
from .views import MerchantViewSet

router = routers.SimpleRouter()
router.register(r'merchants', MerchantViewSet)

urlpatterns = patterns('',
                       url(r'', include(router.urls)),
                       )
