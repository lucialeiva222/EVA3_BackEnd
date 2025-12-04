from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile
from devices.models import Device, Category, Zone

def home(request):
    total_devices = Device.objects.count()
    total_categories = Category.objects.count()
    total_zones = Zone.objects.count()

    last_devices = Device.objects.select_related('category', 'zone').order_by('-id')[:5]

    data = {
        'total_devices': total_devices,
        'total_categories': total_categories,
        'total_zones': total_zones,
        'last_devices': last_devices
    }
    return render(request, 'core/home.html', data)

@login_required 
def profile(request):

    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'core/profile.html', context)