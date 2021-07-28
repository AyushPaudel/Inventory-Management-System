from django.db import models
from ims_users.models import imsUser
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class categories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url_slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='photos/categories/%Y/%m/%d/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class subCategories(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url_slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='photos/subcategories/%Y/%m/%d/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)


class products(models.Model):
    id = models.AutoField(primary_key=True)
    url_slug = models.SlugField(unique=True)
    sub_categories_id = models.ForeignKey(
        subCategories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    product_max_price = models.CharField(max_length=255)
    product_discount_price = models.CharField(max_length=255)
    product_description = models.TextField()
    product_long_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_stock = models.IntegerField(default=1)
    media_content = models.ImageField(blank=True, null=True, upload_to='photos/products/%Y/%m/%d/')
    is_active = models.IntegerField(default=1)

'''
class productMedia(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    media_content = models.ImageField(blank=True, null=True, upload_to='photos/products/%Y/%m/%d/')
    media_content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)
'''

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


class recipt(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(products, on_delete=models.DO_NOTHING)
    purchase_price = models.CharField(max_length=255)
    coupon_code = models.CharField(max_length=255)
    discount_amount = models.CharField(max_length=255)
    product_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


# Making the customer record table:
class customerRecords(models.Model):
    user_id = models.OneToOneField(imsUser, on_delete=models.CASCADE)
    purchased_product_id = models.ForeignKey(recipt, on_delete=models.DO_NOTHING)
    purchased_date = models.DateField()


#Create user in records table if created.
@receiver(post_save, sender=imsUser)
def create_customer_records(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'CU':
            customerRecords.objects.create(user_id=instance)


@receiver(post_save, sender=imsUser)
def save_customer_records(sender, instance, **kwargs):

    if instance.user_type == 'CU':
        instance.customerRecords.save()

