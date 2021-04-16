from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import imsUser


class imsUserCreationForm(UserCreationForm):
    class Meta:
        model = imsUser
        fields = "__all__"
        