from django.contrib import admin
from.models import imsUser
from .forms import imsUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class imsUserAdmin(UserAdmin):
    model = imsUser
    add_form = imsUserCreationForm

    fieldsets = (
            ('Contacts',
               {
                    'fields':
                    (
                        'name',
                        'Landline_number',
                        'mobile_number',
                        'address',
                    )
               }
            ),

            ('User Role',
                {
                    'fields':
                    (
                        'is_employee',
                        'is_customer',
                    )
                }
            )
        )

admin.site.register(imsUser, imsUserAdmin)
