from django.contrib import admin

from .models import Product, CatalogItem

admin.site.register(Product)

admin.site.register(CatalogItem)
