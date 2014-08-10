from django.contrib import admin
from merchant.models import Merchant


class MerchantAdmin(admin.ModelAdmin):
    """Merchant admin customziations"""
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(Merchant, MerchantAdmin)
