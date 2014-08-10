"""Product app related URLs"""
from django.conf.urls import patterns, url, include
from rest_framework_saasy import routers
from .views import ProductViewSet


router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)

urlpatterns = patterns('',
                       url(r'', include(router.urls)),
                       )
