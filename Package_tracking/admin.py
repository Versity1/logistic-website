from django.contrib import admin
from .models import Package
# Register your models here.


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'receiver_name', 'status', 'created_at')
    list_editable = ('status',)
    list_filter = ('status', 'created_at')
