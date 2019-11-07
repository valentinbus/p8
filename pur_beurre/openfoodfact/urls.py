from django.conf.urls import url
from . import views


urlpatterns = [
    url('list/', views.list_all_products),
    url('replace/', views.purpose_replace)
]