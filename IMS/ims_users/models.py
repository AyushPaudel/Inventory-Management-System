from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.



class imsUser(AbstractUser):
    name = models.CharField(max_length=100, blank=False, default="")

    # Contacts
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number should be in correct format'. Up to 15 digits allowed.")

    Landline_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    address = models.CharField(max_length=100, blank=True)

    # user types
    user_type_choices = [(1, "Admin"), (2, "Staff"),
                         (3, "Customer")]
    user_type = models.CharField(
        max_length=255, choices=user_type_choices, default=1)

    def __str__(self):
        return self.username


class adminUser(models.Model):
    profile_pic = models.FileField(default="")
    auth_user_id = models.OneToOneField(imsUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class staffUser(models.Model):
    profile_pic = models.FileField(default="")
    auth_user_id = models.OneToOneField(imsUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class customerUser(models.Model):
    auth_user_id = models.OneToOneField(imsUser, on_delete=models.CASCADE)
    profile_pic = models.FileField(default="")
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=imsUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            adminUser.objects.create(auth_user_id=instance)

        if instance.user_type == 2:
            staffUser.objects.create(auth_user_id=instance)

        if instance.user_type == 3:
            customerUser.objects.create(auth_user_id=instance)


@receiver(post_save, sender=imsUser)
def save_user_profile(sender, instance, **kwargs):

    if instance.user_type == 1:
        instance.adminuser.save()

    if instance.user_type == 2:
        instance.staffuser.save()

    if instance.user_type == 3:
        instance.customeruser.save()
