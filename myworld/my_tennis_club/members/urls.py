from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('members/', views.members, name='members'),
    path('', views.home, name='home'),  
    path('members/', views.members, name='members'),
    path('Vijesti/', views.vijesti, name='vijesti'),
    path('Vijesti/Clanak/<int:id>', views.clanak, name='clanak'),
    path('Upis/', views.upis, name='upis'),
    path('Prostor/', views.prostor, name='prostor'),
    # path('smjerovi/<slug:slug>', views.smijer, name='smijer'),
    path('Događaji/', views.događaji, name='događaji'),
    path('Kontakt/', views.kontakt, name='kontakt'),
    path('Sekcije/', views.sekcije, name='sekcije'),

# This might produce some unwanted bugs:
    path('Struke/', views.struke, name='struke'),
    path('smjerovi/<slug:struka_slug>/<slug:smijer_slug>/', views.struka_smijer_view, name='struka-smijer'),

]