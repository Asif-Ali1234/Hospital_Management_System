from django.contrib import admin
from .models import Authentication
from django.contrib.auth.admin import UserAdmin

class AuthenticationAdmin(UserAdmin):
    model = Authentication
    list_display = ("username","email","is_staff","is_hospital","is_medical","is_user")
    list_filter = ("is_superuser","is_hospital","is_medical","is_user")
    fieldsets = (
        (('Personal info'), {'fields': ('email','first_name', 'last_name','is_user','is_hospital','is_medical')}),
        (('Permissions'),{'fields': ('is_staff', 'is_superuser','user_permissions')}),
        (("Dates"),{'fields': ('last_login', 'date_joined')})
    )

    class Meta:
        model =Authentication

# Register your models here.
admin.site.register(Authentication,AuthenticationAdmin)