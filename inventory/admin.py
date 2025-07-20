from django.contrib import admin
from .models import Equipment

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'category', 'status', 'location', 'is_under_warranty')
    list_filter = ('category', 'status', 'manufacturer')
    search_fields = ('name', 'serial_number', 'manufacturer', 'model_number')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'serial_number', 'category', 'manufacturer', 'model_number')
        }),
        ('Status & Location', {
            'fields': ('status', 'location', 'assigned_user')
        }),
        ('Dates', {
            'fields': ('purchase_date', 'warranty_expiration', 'created_at', 'updated_at')
        }),
    )
