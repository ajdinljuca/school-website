from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('', views.home, name='home'),
    path('smjerovi/', views.smjerovi, name='smjerovi'),
]