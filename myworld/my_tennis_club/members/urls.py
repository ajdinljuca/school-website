from django.urls import path
from . import views
from django.urls import path


smjerovi = ["mehatronika", "mašinstvo", "tekstilstvo"]

urlpatterns = [
    path('members/', views.members, name='members'),
    path('', views.home, name='home'),  
    path('members/', views.members, name='members'),
    path('Vijesti/', views.vijesti, name='vijesti'),
    path('Upis/', views.upis, name='upis'),
    path('Prostor/', views.prostor, name='prostor'),
    path('smjerovi/<slug:slug>', views.smjerovi, name='smjerovi'),
    path('Događaji/', views.događaji, name='događaji'),
    path('Kontakt/', views.kontakt, name='kontakt'),
]