from django import forms
from .models import Equipment, MaintenanceRecord, RepairRecord

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = [
            'name',
            'serial_number',
            'asset_tag',
            'category',
            'manufacturer',
            'model_number',
            'price',
            'purchase_date',
            'warranty_expiration',
            'assigned_user',
            'status',
            'location',
            'notes'
        ]
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'warranty_expiration': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = [
            'date',
            'description',
            'performed_by',
            'cost'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class RepairForm(forms.ModelForm):
    class Meta:
        model = RepairRecord
        fields = [
            'date',
            'issue_description',
            'repair_description',
            'performed_by',
            'cost',
            'completed'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'issue_description': forms.Textarea(attrs={'rows': 3}),
            'repair_description': forms.Textarea(attrs={'rows': 3}),
        }
