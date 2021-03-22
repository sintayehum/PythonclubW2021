from django.shortcuts import render, get_object_or_404
from .models import Product, Pythontype, Club
from django.urls import reverse_lazy
from.forms Import productForm
from django.contrib.auth.descriptions import login_required
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter

def registerPage(request):
   if request.user.is_authenticated:
       return redirect('home')
   else:
       form = CreateUserForm()
       if request.method == 'POST':
           form = CreateUserForm(request.POST)
           if form.is_valid():
               form.save()
               user = form.cleaned_data.get('username')
               messages.success(request, 'Account was created for ' + user)

               return redirect('login')
          

       context = {'form':form}
       return render(request, 'accounts/register.html', context)

def loginPage(request):
   if request.user.is_authenticated:
       return redirect('home')
   else:
       if request.method == 'POST':
           username = request.POST.get('username')
           password =request.POST.get('password')

           user = authenticate(request, username=username, password=password)

           if user is not None:
               login(request, user)
               return redirect('home')
           else:
               messages.info(request, 'Username OR password is incorrect')

       context = {}
       return render(request, 'accounts/login.html', context)

def logoutUser(request):
   logout(request)
   return redirect('login')


@login_required(login_url='login')
def home(request):
   orders = Order.objects.all()
   customers = Customer.objects.all()

   total_customers = customers.count()

   total_orders = orders.count()
   delivered = orders.filter(status='Delivered').count()
   pending = orders.filter(status='Pending').count()

   context = {'orders':orders, 'customers':customers,
   'total_orders':total_orders,'delivered':delivered,
   'pending':pending }

   return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def products(request):
   products = Product.objects.all()

   return render(request, 'accounts/products.html', {'products':products})

@login_required(login_url='login')
def customer(request, pk_test):
   customer = Customer.objects.get(id=pk_test)

   orders = customer.order_set.all()
   order_count = orders.count()

   myFilter = OrderFilter(request.GET, queryset=orders)
   orders = myFilter.qs

   context = {'customer':customer, 'orders':orders, 'order_count':order_count,
   'myFilter':myFilter}
   return render(request, 'accounts/customer.html',context)

@login_required(login_url='login')
def createOrder(request, pk):
   OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
   customer = Customer.objects.get(id=pk)
   formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
   #form = OrderForm(initial={'customer':customer})
   if request.method == 'POST':
       #print('Printing POST:', request.POST)
       form = OrderForm(request.POST)
       formset = OrderFormSet(request.POST, instance=customer)
       if formset.is_valid():
           formset.save()
           return redirect('/')

   context = {'form':formset}
   return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):

   order = Order.objects.get(id=pk)
   form = OrderForm(instance=order)

   if request.method == 'POST':
       form = OrderForm(request.POST, instance=order)
       if form.is_valid():
           form.save()
           return redirect('/')

   context = {'form':form}
   return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
   order = Order.objects.get(id=pk)
   if request.method == "POST":
       order.delete()
       return redirect('/')

   context = {'item':order}
   return render(request, 'accounts/delete.html', context)
#@login_required(login_url='login')
def index(request):
    return render(request,'Club/index.html')

def products(request):
        product_list=Product.objects.all()
        return render(request, 'python/products.html',{'product_list': product_list})

def productDetail(request, id):
    product=get_object_or_404(product, pk=id)
    return render(request,'club/productdetail,html', {'product' : product})

@longin_required
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

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoumessage(request):
    return render(request, 'club/logoumessage.html')
            

