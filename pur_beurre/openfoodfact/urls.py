from django.conf.urls import url
from . import views


urlpatterns = [
    url('search/', views.search),
    url('replace/', views.replace),
]