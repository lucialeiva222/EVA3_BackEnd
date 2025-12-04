import openpyxl 
from django.http import HttpResponse 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator 
from .models import Device, Category, Zone
from .forms import DeviceForm, CategoryForm, ZoneForm

def device_list(request):
    devices = Device.objects.all().order_by('-id')
    
    search_query = request.GET.get('q')
    if search_query:
        devices = devices.filter(name__icontains=search_query)

    category_id = request.GET.get('category')
    if category_id:
        devices = devices.filter(category_id=category_id)

    paginator = Paginator(devices, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'devices': page_obj, 
        'categories': Category.objects.all(),
        'search_query': search_query, 
        'current_category': int(category_id) if category_id else None 
    }
    return render(request, 'devices/device_list.html', data)

@login_required
@permission_required('devices.add_device', raise_exception=True)
def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, '¡Dispositivo creado exitosamente!')
            return redirect('device_list')
    else:
        form = DeviceForm()

    return render(request, 'devices/device_form.html', {'form': form})

@login_required
@permission_required('devices.update_device', raise_exception=True)
def device_update(request, pk):
    device = get_object_or_404(Device, pk=pk)

    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Dispositivo actualizado correctamente!')
            return redirect('device_list')
    else:
        form = DeviceForm(instance=device)

    return render(request, 'devices/device_form.html', {'form': form})

@login_required
@permission_required('devices.delete_device', raise_exception=True)
def device_delete(request, pk):
    device = get_object_or_404(Device, pk=pk)
    device.delete()
    messages.success(request, '¡Dispositivo eliminado correctamente!')
    return redirect('device_list')

def export_devices_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Dispositivos"

    headers = ["Nombre", "Categoría", "Zona", "Modelo", "Fecha Creación"]
    ws.append(headers)

    devices = Device.objects.all().order_by('-id')

    for device in devices:
        ws.append([
            device.name,
            device.category.name, 
            device.zone.name,    
            device.model_number or "--", 
            device.created_at.strftime('%Y-%m-%d') 
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="listado_dispositivos.xlsx"'

    wb.save(response)
    return response

def category_list(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'devices/category_list.html', {'categories': categories})

@login_required
@permission_required('devices.add_category', raise_exception=True)
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Categoría creada exitosamente!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'devices/category_form.html', {'form': form})

@login_required
@permission_required('devices.update_category', raise_exception=True)
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Categoría actualizada!')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'devices/category_form.html', {'form': form})

@login_required
@permission_required('devices.delete_category', raise_exception=True)
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, '¡Categoría eliminada correctamente!')
    return redirect('category_list')

def zone_list(request):
    zones = Zone.objects.all().order_by('name')
    return render(request, 'devices/zone_list.html', {'zones': zones})

@login_required
@permission_required('devices.add_zone', raise_exception=True)
def zone_create(request):
    if request.method == 'POST':
        form = ZoneForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Zona creada exitosamente!')
            return redirect('zone_list')
    else:
        form = ZoneForm()
    return render(request, 'devices/zone_form.html', {'form': form})

@login_required
@permission_required('devices.update_zone', raise_exception=True)
def zone_update(request, pk):
    zone = get_object_or_404(Zone, pk=pk)
    if request.method == 'POST':
        form = ZoneForm(request.POST, instance=zone)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Zona actualizada!')
            return redirect('zone_list')
    else:
        form = ZoneForm(instance=zone)
    return render(request, 'devices/zone_form.html', {'form': form})

@login_required
@permission_required('devices.delete_zone', raise_exception=True)
def zone_delete(request, pk):
    zone = get_object_or_404(Zone, pk=pk)
    zone.delete()
    messages.success(request, '¡Zona eliminada correctamente!')
    return redirect('zone_list')