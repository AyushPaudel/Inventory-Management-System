from django.db import models
from ims_users.models import staffUser, adminUser, customerUser
# Create your models here.


class categories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255)
    thumbnail = models.FileField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class SubCategories(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255)
    thumbnail = models.FileField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class products(models.Model):
    id = models.AutoField(primary_key=True)
    url_slug = models.CharField(max_length=255)
    sub_categories_id = models.ForeignKey(
        subCategories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    product_max_price = models.CharField(max_length=255)
    product_discount_price = models.CharField(max_length=255)
    product_description = models.TextField()
    product_long_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    added_by_staff = models.ForeignKey(staffUser, on_delete=models.CASCADE)
    total_stock = models.IntegerField(default=1)
    is_active = models.IntegerField(default=1)


class productMedia(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    media_type_choice = ((1, "Image"), (2, "Video"))
    media_type = models.CharField(choices=media_type_choice, max_length=255)
    media_content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class productTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    transaction_product_count = models.IntegerField(default=1)
    transaction_type_choices = ((1, "Cash"), (2, "Card"), (3, "Crypto"))
    transaction_type = models.CharField(
        choices=transaction_type_choices, max_length=255)
    transcation_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class productDetails(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    title_details = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class productAbout(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class productTags(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class productVarient(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class productVarientItems(models.Model):
    id = models.AutoField(primary_key=True)
    product_varient_id = models.ForeignKey(
        productVarient, on_delete=models.CASCADE)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class customerOrders(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.DO_NOTHING)
    purchase_price = models.CharField(max_length=255)
    coupon_code = models.CharField(max_length=255)
    discount_amount = models.CharField(max_length=255)
    product_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
