from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('services_details/', views.services_details, name='services_details'),
    path('track/', views.track, name='track'),
]