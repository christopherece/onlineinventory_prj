from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Equipment(models.Model):
    STATUS_CHOICES = [
        ('IN_USE', 'In Use'),
        ('IN_STOCK', 'In Stock'),
        ('UNDER_REPAIR', 'Under Repair'),
        ('RETIRED', 'Retired'),
        ('DECOMMISSIONED', 'Decommissioned'),
    ]

    CATEGORY_CHOICES = [
        ('LAPTOP', 'Laptop'),
        ('MONITOR', 'Monitor'),
        ('MOUSE', 'Mouse'),
        ('KEYBOARD', 'Keyboard'),
        ('HEADSET', 'Headset'),
        ('PHONE', 'Phone'),
        ('ROUTER', 'Router'),
        ('SWITCH', 'Switch'),
        ('DESKTOP', 'Desktop'),
        ('PRINTER', 'Printer'),
        ('SERVER', 'Server'),
        ('STORAGE', 'Storage Device'),
        ('NETWORK', 'Network Device'),
        ('OTHER', 'Other'),
    ]

    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    asset_tag = models.CharField(max_length=20, unique=True, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    manufacturer = models.CharField(max_length=100)
    model_number = models.CharField(max_length=50)
    purchase_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Purchase price in USD")
    warranty_expiration = models.DateField()
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='assigned_equipment', help_text="User assigned to this equipment")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='IN_STOCK')
    location = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    decommission_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"

    def is_under_warranty(self):
        return self.warranty_expiration > timezone.now().date()

    def is_decommissioned(self):
        return self.status == 'DECOMMISSIONED'

    def total_days_in_use(self):
        if self.status == 'RETIRED' or self.status == 'DECOMMISSIONED':
            return (self.decommission_date or timezone.now().date()) - self.purchase_date
        return timezone.now().date() - self.purchase_date

    class Meta:
        ordering = ['-created_at']

class MaintenanceRecord(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='maintenance_records')
    date = models.DateField()
    description = models.TextField()
    performed_by = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Maintenance for {self.equipment.name} on {self.date}"

class RepairRecord(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='repair_records')
    date = models.DateField()
    issue_description = models.TextField()
    repair_description = models.TextField()
    performed_by = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Repair for {self.equipment.name} on {self.date}"

class LifecycleEvent(models.Model):
    EVENT_CHOICES = [
        ('PURCHASED', 'Purchased'),
        ('INSTALLED', 'Installed'),
        ('REPAIRED', 'Repaired'),
        ('MAINTAINED', 'Maintained'),
        ('REPLACED', 'Replaced'),
        ('RETIRED', 'Retired'),
        ('DECOMMISSIONED', 'Decommissioned'),
    ]

    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='lifecycle_events')
    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_event_type_display()} for {self.equipment.name} on {self.date}"
