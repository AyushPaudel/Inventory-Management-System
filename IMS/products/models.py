from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    type = models.CharField(max_length=200)
    subtype: models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=150)



class Product(ProductCategory):

    name = models.CharField(max_length=300)
    description = models.TextField()
    photo = models.ImageField(upload_to="product", blank=False)
    manufacturer = models.CharField(max_length=300, blank=True)
    price_in_rupees = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    buying_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_id = models.AutoField(primary_key=True)
    # barcode =



