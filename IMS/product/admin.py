from django.contrib import admin
from .models import categories, subCategories, products, Recipt, customerRecords
# Register your models here.


admin.site.register(Recipt)
admin.site.register(customerRecords)


@admin.register(categories)
class categoriesAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_filter = ("created_at",)


@admin.register(subCategories)
class subCategoriesAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    list_filter = ("category_id",)


@admin.register(products)
class productsAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_max_price", "total_stock")
    list_filter = ("sub_categories_id",)


