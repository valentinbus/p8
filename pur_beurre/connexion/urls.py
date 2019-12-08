from django.urls import path
from django.contrib.auth import views

from . import views

urlpatterns = [
    path('', views.connexion),
    path('deconnexion', views.deconnexion),
    path('registration', views.registration),
]
