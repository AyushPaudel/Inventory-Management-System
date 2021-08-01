from django.db import models
from ims_users.models import imsUser
from django.dispatch import receiver
from django.db.models.signals import m2m_changed, post_save

from datetime import datetime
import uuid 
# Create your models here.


class categories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url_slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='photos/categories/%Y/%m/%d/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

    def __str__(self):
        return(str(self.title))


class subCategories(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url_slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='photos/subcategories/%Y/%m/%d/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.IntegerField(default=1)

    def __str__(self):
        return(str(self.title))


class products(models.Model):
    id = models.AutoField(primary_key=True)
    url_slug = models.SlugField(unique=True)
    sub_categories_id = models.ForeignKey(
        subCategories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    product_max_price = models.PositiveIntegerField(default=0)
    product_discount_price = models.PositiveIntegerField(default=0)
    product_description = models.TextField()
    product_long_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    original_stock = models.PositiveIntegerField(default=1)
    total_stock = models.PositiveIntegerField(default=1)
    
    media_content = models.ImageField(blank=True, null=True, upload_to='photos/products/%Y/%m/%d/')
    is_active = models.IntegerField(default=1)

    def __str__(self):
        return str(self.product_name)

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


class Recipt(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ManyToManyField(products)
    quantity = models.TextField(blank=False)
    purchase_price = models.PositiveIntegerField(default=0)
    discount_amount = models.PositiveIntegerField(default=0)
    total_items = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    unique_token = models.CharField(max_length=10, blank=True)
    redeemed = models.BooleanField(default=False)

    def __str__(self):
        return(str(self.unique_token))


# Making the customer record table:
class customerRecords(models.Model):
    imsuser = models.OneToOneField(imsUser, on_delete=models.CASCADE)
    recipt = models.ManyToManyField(Recipt)
    total_expenditure = models.PositiveIntegerField(default=0)


    def __str__(self):
        return (str(self.imsuser))


#Create user in records table if created.
@receiver(post_save, sender=imsUser)
def create_customer_records(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'CU':
            customerRecords.objects.create(imsuser=instance)


# Alter recipt when product is added. 
@receiver(m2m_changed, sender=Recipt.product.through)
def m2m_changed_recipt_product(sender, instance, action, **kwargs):
    total_items = 0
    total_price = 0
    discount = 0
    
    if action == 'post_add' or action == 'post_remove':
        index = 0
        quantity = instance.quantity.split(',')
        for product in instance.product.all():
            total_items += int(quantity[index])
            total_price += product.product_max_price*total_items 
            discount += product.product_discount_price
            index+=1

        instance.purchase_price = total_price
        instance.discount_amount = discount
        instance.total_items = total_items

        # Generating Unique Tokens:
        if instance.unique_token == "":
            instance.unique_token = str(uuid.uuid4()).replace("-", "").upper()[:10]

        instance.save()


@receiver(m2m_changed, sender=customerRecords.recipt.through)
def m2m_changed_recipt_product(sender, instance, action, **kwargs):
    total_recipts = 0
    total_expenditure = 0
    
    if action == 'post_add' or action == 'post_remove':
        print(action)
        for recipt in instance.recipt.all():
            total_recipts +=1
            total_expenditure += recipt.purchase_price

        instance.total_expenditure = total_expenditure
        instance.save()





    

