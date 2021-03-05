from django.urls import path
from PobrezaHM import views

urlpatterns = [
    path('', views.home, name="home"),
    path('mapa', views.mapa, name="mapa"),
]