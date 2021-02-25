from django.shortcuts import render
from .models import Product, Pythontype, Club

# Create your views here.
def index(request):
    return render(request,'Club/index.html')


def products(request):
        product_list=Product.objects.all()
        return render(request, 'python/products.html',{'product_list': product_list})