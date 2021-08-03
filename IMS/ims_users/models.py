from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.timezone import now
# Create your models here.


class imsUser(AbstractUser):
    name = models.CharField(max_length=100, blank=False, default="")

    # Contacts
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number should be in correct format'. Up to 15 digits allowed.")

    Landline_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    mobile_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)

    address = models.CharField(max_length=100, blank=True)
    profile_pic = models.FileField(default="")
    pay = models.IntegerField(default=0)

    # user types
    user_type_choices = [
        ('AD', 'Admin'),
        ('ST', 'Staff'),
        ('CU', 'Customer'),
    ]
    user_type = models.CharField(
        max_length=255, choices=user_type_choices, default='AD')
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.username

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(imsUser, on_delete=models.CASCADE)
    paid_money = models.IntegerField()
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff.username + ' ' + str(self.paid_money)

'''
class adminUser(models.Model):
    auth_user_id = models.OneToOneField(imsUser, on_delete=models.CASCADE)
    


class staffUser(models.Model):
    auth_user_id = models.OneToOneField(imsUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class customerUser(models.Model):
    auth_user_id = models.OneToOneField(imsUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=imsUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'AD':
            adminUser.objects.create(auth_user_id=instance)

        if instance.user_type == 'ST':
            staffUser.objects.create(auth_user_id=instance)

        if instance.user_type == 'CU':
            customerUser.objects.create(auth_user_id=instance)


@receiver(post_save, sender=imsUser)
def save_user_profile(sender, instance, **kwargs):

    if instance.user_type == 'AD':
        instance.adminuser.save()

    if instance.user_type == 'ST':
        instance.staffuser.save()

    if instance.user_type == 'CU':
        instance.customeruser.save()
'''

