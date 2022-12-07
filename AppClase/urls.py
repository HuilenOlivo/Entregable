from django.urls import path
from AppClase.views import*

urlpatterns= [
    path ('familiares/', familiares, name='familiares'),
    
]