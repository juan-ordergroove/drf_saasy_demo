"""Merchant app related models"""
from django.db import models
from django.template.defaultfilters import slugify

import django.db.models.options as options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + (
    'saas_url_param',
    'saas_lookup_field',
    )


class Merchant(models.Model):
    """Merchant/client data model"""
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        saas_url_param = 'merchant_slug'
        saas_lookup_field = 'slug'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Merchant, self).save(self, *args, **kwargs)

    def __unicode__(self):
        return u'{}'.format(self.name)
