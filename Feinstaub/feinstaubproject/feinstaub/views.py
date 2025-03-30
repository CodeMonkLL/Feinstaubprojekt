from django.shortcuts import render

from django.shortcuts import render
from .models import DHT22Metric, SDS011Metric

def my_view_DHT(request):
    items = DHT22Metric.objects.all()
    return render(request, 'feinstaub/template.html', {'items': items})

def my_view_SDS(request):
    items = SDS011Metric.objects.all()
    return render(request, 'feinstaub/template.html', {'items': items})

