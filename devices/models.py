from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre de Categoría")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Fecha eliminación")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Zone(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre de Zona")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Fecha eliminación")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Zona"
        verbose_name_plural = "Zonas"

class Device(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Dispositivo")
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoría")
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, verbose_name="Zona")
    
    model_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="Modelo/Serie")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Fecha eliminación")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"