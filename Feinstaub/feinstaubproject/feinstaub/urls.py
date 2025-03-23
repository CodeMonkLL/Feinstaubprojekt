from django.urls import path
from .views import my_view_DHT, my_view_SDS

urlpatterns = [
    path('', my_view_DHT, name='home'),
    path('', my_view_SDS, name='home'),
]