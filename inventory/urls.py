from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.equipment_list, name='list'),
    path('equipment/<int:pk>/', views.equipment_detail, name='detail'),
    path('equipment/new/', views.equipment_create, name='create'),
    path('equipment/<int:pk>/edit/', views.equipment_edit, name='edit'),
    path('equipment/<int:pk>/delete/', views.equipment_delete, name='delete'),
    path('equipment/<int:pk>/maintenance/new/', views.add_maintenance, name='add_maintenance'),
    path('equipment/<int:pk>/repair/new/', views.add_repair, name='add_repair'),
]
