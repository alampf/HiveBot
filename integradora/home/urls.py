from django.urls import path  # type: ignore
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca/', views.acerca, name='acerca'),
    path('asesoramiento/', views.asesoramiento, name='asesoramiento'),
    path('contacto/', views.contacto, name='contacto'),
]
