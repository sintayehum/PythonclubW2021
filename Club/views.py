from django.shortcuts import render, get_object_or_404
from .models import Product, Pythontype, Club
from django.urls import reverse_lazy
from.forms Import productForm
# Create your views here.
def index(request):
    return render(request,'Club/index.html')

def products(request):
        product_list=Product.objects.all()
        return render(request, 'python/products.html',{'product_list': product_list})

def productDetail(request, id):
    product=get_object_or_404(product, pk=id)
    return render(request,'club/productdetail,html', {'product' : product})

    def newProduct(request):
        form=ProductForm

        if request. method=='post':
            from=ProductForm(request.post)
            if form.is_valid():
                post=form.save(commit=True)
                post.save()
                form=ProductForm()
        else:
            form=ProductForm()
        return render(request, 'club/newproduct.html', {'form': form})
            

