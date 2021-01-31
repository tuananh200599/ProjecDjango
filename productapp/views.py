from django.shortcuts import render
from django.http import HttpResponse
from productapp.models import Product

def home(request):
    Data = {'Products': Product.objects.all()}
    return render(request, 'products/produt.html', Data)
def detail(request, id):
    detail = Product.objects.get(id=id)
    return render(request, 'products/detail.html',{'Products' : detail})
