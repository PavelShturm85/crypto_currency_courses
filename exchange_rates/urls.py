from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.exchange_rates_list, name='exchange_rates_list'),
]