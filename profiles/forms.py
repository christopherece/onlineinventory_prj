from django import forms
from .models import Profile

class ProfileSearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        label='Search',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search by name, username, department, or position'
        })
    )
    department = forms.CharField(
        required=False,
        label='Department',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    position = forms.CharField(
        required=False,
        label='Position',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'full_name',
            'department',
            'position',
            'employee_id',
            'phone_number',
            'emergency_contact',
            'emergency_phone',
            'photo',
            'date_of_birth',
            'hire_date'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
            'photo': forms.FileInput(attrs={'accept': 'image/*'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({'class': 'form-control'})
