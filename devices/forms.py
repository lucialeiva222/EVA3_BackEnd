from django import forms
from .models import Device, Category, Zone

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'category', 'zone', 'model_number']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Sensor de Humedad'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'zone': forms.Select(attrs={'class': 'form-select'}),
            'model_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Opcional'}),
        }
        
        labels = {
            'name': 'Nombre del Dispositivo',
            'category': 'Categoría',
            'zone': 'Zona de Ubicación',
            'model_number': 'Número de Serie / Modelo',
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name'] 
        labels = {
            'name': 'Nombre de la Categoría',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Iluminación, Sensores...'}),
        }

class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ['name']
        labels = {
            'name': 'Nombre de la Zona',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Planta Baja, Almacén...'}),
        }