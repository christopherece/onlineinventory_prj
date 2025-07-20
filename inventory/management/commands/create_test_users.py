from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from profiles.models import Profile
import random

class Command(BaseCommand):
    help = 'Create test users with Emma'

    def handle(self, *args, **options):
        # Create test users
        test_users = [
            {'username': 'emma.smith', 'full_name': 'Emma Smith', 'department': 'IT', 'position': 'Developer'},
            {'username': 'emma.johnson', 'full_name': 'Emma Johnson', 'department': 'HR', 'position': 'Recruiter'},
            {'username': 'emily.davis', 'full_name': 'Emily Davis', 'department': 'Marketing', 'position': 'Manager'},
        ]

        for user_data in test_users:
            try:
                user = User.objects.create_user(
                    username=user_data['username'],
                    password='testpassword123',
                    email=f"{user_data['username']}@example.com"
                )
                Profile.objects.create(
                    user=user,
                    full_name=user_data['full_name'],
                    department=user_data['department'],
                    position=user_data['position'],
                    employee_id=f"EMP{random.randint(1000, 9999)}"
                )
                self.stdout.write(self.style.SUCCESS(f'Created user: {user_data["full_name"]}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating user: {str(e)}'))
