from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Equipment, MaintenanceRecord, RepairRecord, LifecycleEvent
from .forms import EquipmentForm, MaintenanceForm, RepairForm

def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'inventory/equipment_list.html', {'equipment': equipment})

def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    maintenance_records = equipment.maintenance_records.all().order_by('-date')
    repair_records = equipment.repair_records.all().order_by('-date')
    lifecycle_events = equipment.lifecycle_events.all().order_by('-date')
    
    return render(request, 'inventory/equipment_detail.html', {
        'equipment': equipment,
        'maintenance_records': maintenance_records,
        'repair_records': repair_records,
        'lifecycle_events': lifecycle_events
    })

def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save()
            # Create a lifecycle event for purchase
            LifecycleEvent.objects.create(
                equipment=equipment,
                event_type='PURCHASED',
                date=equipment.purchase_date
            )
            messages.success(request, 'Equipment created successfully')
            return redirect('inventory:detail', pk=equipment.pk)
    else:
        form = EquipmentForm()
    return render(request, 'inventory/equipment_form.html', {
        'form': form,
        'users': User.objects.all(),
        'title': 'Add Equipment'
    })

def equipment_edit(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            equipment = form.save()
            messages.success(request, 'Equipment updated successfully')
            return redirect('inventory:detail', pk=equipment.pk)
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'inventory/equipment_form.html', {
        'form': form,
        'users': User.objects.all(),
        'title': 'Edit Equipment'
    })

def equipment_delete(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment.delete()
        messages.success(request, 'Equipment deleted successfully')
        return redirect('equipment_list')
    return render(request, 'inventory/equipment_confirm_delete.html', {'equipment': equipment})

def add_maintenance(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            maintenance = form.save(commit=False)
            maintenance.equipment = equipment
            maintenance.save()
            # Create a lifecycle event
            LifecycleEvent.objects.create(
                equipment=equipment,
                event_type='MAINTAINED',
                date=maintenance.date
            )
            messages.success(request, 'Maintenance record added successfully')
            return redirect('equipment_detail', pk=pk)
    else:
        form = MaintenanceForm()
    return render(request, 'inventory/maintenance_form.html', {
        'form': form,
        'equipment': equipment,
        'title': 'Add Maintenance'
    })

def add_repair(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.equipment = equipment
            repair.save()
            # Create a lifecycle event
            if repair.completed:
                event_type = 'REPAIRED'
            else:
                event_type = 'REPAIRED'
            LifecycleEvent.objects.create(
                equipment=equipment,
                event_type=event_type,
                date=repair.date
            )
            messages.success(request, 'Repair record added successfully')
            return redirect('equipment_detail', pk=pk)
    else:
        form = RepairForm()
    return render(request, 'inventory/repair_form.html', {
        'form': form,
        'equipment': equipment,
        'title': 'Add Repair'
    })
