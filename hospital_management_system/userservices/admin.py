from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import opcard,bills
# Register your models here.

class billAdmin(admin.ModelAdmin):
    model = bills
    list_display = ("patientemail","medicines_provided","total_amount","bill_status","date_requested")
    list_filter = ("bill_status","medicines_provided","date_requested")

    class Meta:
        model = bills

class opAdmin(admin.ModelAdmin):
    model=opcard
    list_display = ("patientemail","temperature","date_updated")

    class Meta:
        model = opcard

admin.site.register(opcard,opAdmin)
admin.site.register(bills,billAdmin)