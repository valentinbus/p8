from django.conf.urls import url
from . import views


urlpatterns = [
    url('list/', views.list_all_products, name='list'),
    url('replace/', views.purpose_replace, name='replace'),
    url('save_replacement/', views.save_replacement, name='save_replacement'),
    url('search_product/', views.search_product, name='search_product'),
    url('saves/', views.show_saves, name='saves'),
    url('more_informations/', views.more_informations, name='more_informations'),
]