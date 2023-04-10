from django.urls import path
from . import views
from django.urls import path


smjerovi = ["mehatronika", "mašinstvo", "tekstilstvo"]

urlpatterns = [
    path('members/', views.members, name='members'),
    path('', views.home, name='home'),
    path('smjerovi/<slug:slug>', views.smjerovi, name='smjerovi'),
]