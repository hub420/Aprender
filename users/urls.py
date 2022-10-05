""" Definimos los patrones urls para users"""

from atexit import register
from django.urls import path, include


from .import views

app_name = 'users'
urlpatterns = [
   # incluye auth urls por defecto
    path('', include('django.contrib.auth.urls')), 
    # pagina de registro
    path('register/', views.register, name='register'), 
]

 