from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from .models import Product,Delivery
import string
import random

@login_required
def products(request):
    context={}
    products=Product.objects.all()
    context['products']=products
    return render(request,'products.html',context)


@login_required
def buyProduct(request,id=None):
    context={}
    product=Product.objects.get(pk=id)
    context['product']=product

    if request.method=="POST":
        quantity=request.POST['quantity']
        total_bill=int(quantity)*product.price
        print(total_bill)
        shipment_id= ''.join(random.choices(string.ascii_uppercase +string.digits, k = 10))
        Delivery.objects.create(product=product,quantity=quantity,shipment_id=shipment_id,delivery_owner=request.user,total_bill=total_bill)
        messages.success(request,"Order recieved successfully Thank You for being with us")
        return redirect('home')
    else:
        #print(product)
        return render(request,'buy_product.html',context)