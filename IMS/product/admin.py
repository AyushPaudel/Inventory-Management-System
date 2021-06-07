from django.contrib import admin
from .models import categories, subCategories, products
# Register your models here.

admin.site.register(categories)
admin.site.register(subCategories)
admin.site.register(products)