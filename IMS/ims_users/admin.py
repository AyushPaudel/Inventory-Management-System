from django.contrib import admin
from .models import imsUser,Payment
from .forms import imsUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Payment)
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
                        'user_type',
                    )
                }
            )
        )

admin.site.register(imsUser, imsUserAdmin)
