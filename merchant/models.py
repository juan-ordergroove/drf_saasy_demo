"""Merchant app related models"""
from django.db import models
from django.template.defaultfilters import slugify


class Merchant(models.Model):
    """Merchant/client data model"""
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def saas_lookup_field():
        """DRF-SaaS lookup field definition"""
        return 'slug'

    def saas_client_module(self, saas_url_kw, *args, **kwargs):
        """DRF-SaaS client customization module"""
        return 'customizations.{}'.format(self.slug)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Merchant, self).save(self, *args, **kwargs)

    def __unicode__(self):
        return u'{}'.format(self.name)
