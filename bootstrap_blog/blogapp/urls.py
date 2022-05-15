from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('ingreso/', views.ingreso, name='ingreso'),
    path('proveedor/', views.ingresoproveedor, name='proveedor'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
]