from django.contrib import admin
from .models import Product


class ProductArmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = Product


admin.site.register(Product, ProductArmin)
