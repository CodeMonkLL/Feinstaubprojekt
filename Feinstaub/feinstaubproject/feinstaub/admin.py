from django.contrib import admin

from django.contrib import admin
from .models import SDS011Metric, DHT22Metric

admin.site.register(SDS011Metric)
admin.site.register(DHT22Metric)