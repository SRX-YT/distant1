from django.urls import path
from . import views

urlpatterns = [
    path('', views.get, name='get'),
    path('info/', views.get_info, name='get_info'),
]