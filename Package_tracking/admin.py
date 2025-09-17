from django.contrib import admin
from .models import Package
# Register your models here.


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'receiver_name', 'status', 'created_at', 'expected_delivery_date', 'delivery_address', 'current_location', 'from_location', 'to_location')
    list_editable = ('status',)
    list_filter = ('status', 'created_at')
