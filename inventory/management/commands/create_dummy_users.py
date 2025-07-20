from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random
import string

class Command(BaseCommand):
    help = 'Create 20 dummy users with random data'

    def handle(self, *args, **options):
        first_names = [
            'John', 'Emma', 'Michael', 'Sophia', 'William',
            'Olivia', 'James', 'Ava', 'Benjamin', 'Isabella',
            'Lucas', 'Mia', 'Henry', 'Charlotte', 'Alexander',
            'Amelia', 'Daniel', 'Evelyn', 'Matthew', 'Abigail'
        ]

        last_names = [
            'Smith', 'Johnson', 'Williams', 'Brown', 'Jones',
            'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez',
            'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson',
            'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin'
        ]

        for i in range(20):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            username = f"user_{i+1}"
            email = f"user{i+1}@example.com"
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            
            self.stdout.write(self.style.SUCCESS(f'Created user: {username} ({first_name} {last_name})'))

        self.stdout.write(self.style.SUCCESS('Successfully created 20 dummy users'))
