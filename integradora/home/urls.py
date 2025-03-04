from django.urls import path  # type: ignore
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca/', views.acerca, name='acerca'),
    path('asesoramiento/', views.asesoramiento, name='asesoramiento'),
    path('contacto/', views.contacto, name='contacto'),
    
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('registro/', views.registro_view, name = 'registro'),
]
