from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_list, name='device_list'),
    path('create/', views.device_create, name='device_create'),
    path('edit/<int:pk>/', views.device_update, name='device_update'), 
    path('delete/<int:pk>/', views.device_delete, name='device_delete'), 
    path('export/excel/', views.export_devices_excel, name='export_devices_excel'), 
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/edit/<int:pk>/', views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
    path('zones/', views.zone_list, name='zone_list'),
    path('zones/create/', views.zone_create, name='zone_create'),
    path('zones/edit/<int:pk>/', views.zone_update, name='zone_update'),
    path('zones/delete/<int:pk>/', views.zone_delete, name='zone_delete'),
]