# Generated by Django 5.2.4 on 2025-07-20 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=50, unique=True)),
                ('category', models.CharField(choices=[('LAPTOP', 'Laptop'), ('MONITOR', 'Monitor'), ('ROUTER', 'Router'), ('SWITCH', 'Switch'), ('DESKTOP', 'Desktop'), ('PRINTER', 'Printer'), ('OTHER', 'Other')], max_length=20)),
                ('manufacturer', models.CharField(max_length=100)),
                ('model_number', models.CharField(max_length=50)),
                ('purchase_date', models.DateField()),
                ('warranty_expiration', models.DateField()),
                ('assigned_user', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('IN_USE', 'In Use'), ('IN_STOCK', 'In Stock'), ('UNDER_REPAIR', 'Under Repair'), ('RETIRED', 'Retired')], default='IN_STOCK', max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
