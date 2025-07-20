import random
import string
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from inventory.models import Equipment, MaintenanceRecord, RepairRecord, LifecycleEvent

class Command(BaseCommand):
    help = 'Creates dummy equipment entries with maintenance and repair records'

    def generate_serial_number(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def generate_asset_tag(self):
        return f'AS-{random.randint(1000, 9999)}'

    def generate_date_in_range(self, start_years_ago, end_years_ago):
        start_date = timezone.now() - timedelta(days=365 * start_years_ago)
        end_date = timezone.now() - timedelta(days=365 * end_years_ago)
        return start_date + timedelta(
            seconds=random.randint(0, int((end_date - start_date).total_seconds()))
        )

    def handle(self, *args, **options):
        manufacturers = [
            'Dell', 'HP', 'Lenovo', 'Apple', 'Cisco', 'Netgear', 'Brother', 'Epson',
            'Western Digital', 'Seagate', 'Samsung', 'D-Link', 'TP-Link', 'Microsoft'
        ]

        categories = [
            'LAPTOP', 'MONITOR', 'ROUTER', 'SWITCH', 'DESKTOP', 'PRINTER', 'SERVER',
            'STORAGE', 'NETWORK', 'OTHER'
        ]

        statuses = ['IN_USE', 'IN_STOCK', 'UNDER_REPAIR', 'RETIRED', 'DECOMMISSIONED']

        locations = [
            'Main Office', 'Server Room', 'Conference Room', 'Storage Room',
            'Reception Area', 'IT Department', 'Finance Department',
            'Human Resources', 'Marketing Department', 'Engineering Department'
        ]

        self.stdout.write('Creating dummy devices...')

        for i in range(30):
            # Generate random data
            category = random.choice(categories)
            manufacturer = random.choice(manufacturers)
            model = f'Model-{random.randint(100, 999)}'
            purchase_date = self.generate_date_in_range(5, 1)
            warranty_years = random.randint(1, 3)
            warranty_expiration = purchase_date + timedelta(days=warranty_years * 365)
            status = random.choice(statuses)
            location = random.choice(locations)
            assigned_user = f'User{random.randint(1, 100)}' if random.random() < 0.7 else None
            
            # Create equipment
            equipment = Equipment.objects.create(
                name=f'{manufacturer} {model}',
                serial_number=self.generate_serial_number(),
                asset_tag=self.generate_asset_tag(),
                category=category,
                manufacturer=manufacturer,
                model_number=model,
                purchase_date=purchase_date.date(),
                purchase_price=random.uniform(100, 5000),
                warranty_expiration=warranty_expiration.date(),
                assigned_user=assigned_user,
                status=status,
                location=location,
                notes=f'This is a dummy {category.lower()} device.'
            )

            # Create purchase lifecycle event
            LifecycleEvent.objects.create(
                equipment=equipment,
                event_type='PURCHASED',
                date=purchase_date.date(),
                notes='Initial purchase'
            )

            # Add random maintenance records
            for _ in range(random.randint(0, 3)):
                maintenance_date = self.generate_date_in_range(5, 0)
                MaintenanceRecord.objects.create(
                    equipment=equipment,
                    date=maintenance_date.date(),
                    description=f'Regular maintenance for {equipment.name}',
                    performed_by=f'Tech{random.randint(1, 10)}',
                    cost=random.uniform(50, 500)
                )
                LifecycleEvent.objects.create(
                    equipment=equipment,
                    event_type='MAINTAINED',
                    date=maintenance_date.date(),
                    notes='Regular maintenance performed'
                )

            # Add random repair records
            for _ in range(random.randint(0, 2)):
                repair_date = self.generate_date_in_range(5, 0)
                RepairRecord.objects.create(
                    equipment=equipment,
                    date=repair_date.date(),
                    issue_description=f'Issue with {equipment.name}',
                    repair_description=f'Repaired {equipment.name}',
                    performed_by=f'Tech{random.randint(1, 10)}',
                    cost=random.uniform(100, 1000),
                    completed=True
                )
                LifecycleEvent.objects.create(
                    equipment=equipment,
                    event_type='REPAIRED',
                    date=repair_date.date(),
                    notes='Repair completed'
                )

            # Add random decommissioning if status is retired or decommissioned
            if status in ['RETIRED', 'DECOMMISSIONED']:
                decommission_date = self.generate_date_in_range(5, 0)
                equipment.decommission_date = decommission_date.date()
                equipment.save()
                LifecycleEvent.objects.create(
                    equipment=equipment,
                    event_type=status.upper(),
                    date=decommission_date.date(),
                    notes='Device decommissioned'
                )

        self.stdout.write(self.style.SUCCESS('Successfully created 30 dummy devices'))
