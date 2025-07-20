from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'department', 'position', 'phone_number')
    list_filter = ('department', 'position')
    search_fields = ('user__username', 'full_name', 'department')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'full_name', 'employee_id', 'photo')
        }),
        ('Contact Information', {
            'fields': ('phone_number', 'emergency_contact', 'emergency_phone')
        }),
        ('Employment Information', {
            'fields': ('department', 'position', 'date_of_birth', 'hire_date')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at')
        })
    )
