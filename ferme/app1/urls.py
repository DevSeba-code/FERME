from django.urls import path
from . import views




urlpatterns = [
    path('', views.vista_cli_home),
    path('login/', views.login),
   
  
]
