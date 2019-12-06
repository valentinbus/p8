from django.conf.urls import url
from . import views


urlpatterns = [
    url('list/', views.list_all_products),
    url('replace/', views.purpose_replace),
    url('save_replacement/', views.save_replacement),
    url('search_product/', views.search_product),
    url('saves/', views.show_saves),
    url('more_informations/', views.more_informations),
    url('test/', views.test)
]