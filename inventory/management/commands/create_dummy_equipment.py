from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from random import randint, choice
from datetime import timedelta
from inventory.models import Equipment

class Command(BaseCommand):
    help = 'Create 30 dummy equipment entries with random data'

    def handle(self, *args, **options):
        # Get all users we created earlier
        users = User.objects.all()
        
        # Equipment data
        manufacturers = [
            'Dell', 'HP', 'Lenovo', 'Apple', 'Samsung',
            'Logitech', 'Microsoft', 'Cisco', 'Brother', 'Canon'
        ]
        
        locations = [
            'Main Office', 'Conference Room', 'IT Department',
            'Warehouse', 'Reception', 'Meeting Room 1', 'Meeting Room 2',
            'Executive Suite', 'Training Room', 'Storage'
        ]
        
        for i in range(30):
            # Generate random data
            name = f"Device {i+1}"
            serial_number = f"SN{randint(1000000, 9999999)}"
            category = choice(Equipment.CATEGORY_CHOICES)[0]
            manufacturer = choice(manufacturers)
            model_number = f"M{randint(1000, 9999)}"
            
            # Random dates in the last 5 years
            days_offset = randint(0, 1825)  # 5 years in days
            purchase_date = timezone.now() - timedelta(days=days_offset)
            warranty_days = randint(365, 730)  # 1-2 years warranty
            warranty_expiration = purchase_date + timedelta(days=warranty_days)
            
            # Random price between $100 and $5000
            price = randint(100, 5000)
            
            # Randomly assign to a user
            assigned_user = choice(users) if randint(0, 1) == 1 else None
            
            # Random status
            status = choice(Equipment.STATUS_CHOICES)[0]
            
            # Random location
            location = choice(locations)
            
            # Create equipment
            Equipment.objects.create(
                name=name,
                serial_number=serial_number,
                category=category,
                manufacturer=manufacturer,
                model_number=model_number,
                purchase_date=purchase_date,
                warranty_expiration=warranty_expiration,
                assigned_user=assigned_user,
                status=status,
                location=location,
                price=price,
                notes=f"Dummy equipment {i+1} created on {timezone.now().date()}"
            )
            
            self.stdout.write(self.style.SUCCESS(f'Created equipment: {name} ({category})'))

        self.stdout.write(self.style.SUCCESS('Successfully created 30 dummy equipment entries'))
