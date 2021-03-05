from django.urls import path
from PobrezaHM import views

urlpatterns = [
    path('', views.mapa, name="mapa"),
    
]