from django.shortcuts import render
from django.http import HttpResponse
from productapp.models import Product

def home(request):
    Data = {'Products': Product.objects.all()}
    return render(request, 'products/produt.html', Data)