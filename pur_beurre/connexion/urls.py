from django.urls import path
from django.contrib.auth import views

from . import views

urlpatterns = [
    path('', views.connexion, name="connexion"),
    path('deconnexion', views.deconnexion, name="deconnexion"),
    path('registration', views.registration, name="registration"),
]
