from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact'),
    path('contact/confirm/', views.contact_confirm, name='contact_confirm'),
]