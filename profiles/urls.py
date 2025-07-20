from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('profile/', views.profile_detail, name='detail'),
    path('profile/<str:username>/', views.profile_detail, name='detail'),
    path('profile/edit/', views.profile_edit, name='edit'),
    path('profiles/', views.profile_list, name='list'),
]
