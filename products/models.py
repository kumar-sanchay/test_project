from django.db import models
from django.utils.text import slugify
from .manager import Active, Inactive


class Product(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False,
                            verbose_name='Product Name')
    slug = models.SlugField(max_length=50)
    weight = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False,
                                 verbose_name='Product Weight')
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False,
                                verbose_name='Product Price')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    active_obj = Active()
    inactive_obj = Inactive()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_at']
        app_label = 'products'

    def __str__(self):
        return '{}::{}'.format('Product', self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)