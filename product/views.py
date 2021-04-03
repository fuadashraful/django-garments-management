from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from .models import Product,Delivery,Query,Employee
from .forms import EmployeeForm
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
        #print(total_bill)
        shipment_id= ''.join(random.choices(string.ascii_uppercase +string.digits, k = 10))
        Delivery.objects.create(product=product,quantity=quantity,shipment_id=shipment_id,delivery_owner=request.user,total_bill=total_bill)
        messages.success(request,"Order recieved successfully Thank You for being with us")
        return redirect('home')
    else:
        #print(product)
        return render(request,'buy_product.html',context)


def about(request):

    if request.method=="POST":
        #print(request.POST)
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        message=request.POST['message']
        Query.objects.create(first_name=first_name,last_name=last_name,email=email,message=message)
        messages.success(request,"Your message recieved You will be replied soon . Thank You")
        return redirect('home')
    else:
        return render(request,'about_us.html')

@login_required
def allOrders(request):
    context={}
    orders=Delivery.objects.all()
    context['orders']=orders
    return render(request,'admin/all_orders.html',context)

@login_required
def deleteOrder(request,id=None):
    order=Delivery.objects.get(pk=id)
    order.delete()
    messages.warning(request,"This Order deleted successfully")
    return redirect('all_orders')

@login_required
def addEmployee(request):

    context={}
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            #print("form is valid")
            employee=form.save(commit=False)
            employee.save()
            messages.success(request,"Employee Saved Successfully")
        return redirect('profile',id=request.user.id)
    else:
        form=EmployeeForm()
        context['form']=form
    return render(request,'admin/add_employee.html',context)

@login_required
def deleteEmployee(request,id=None):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    messages.warning(request,"Employee deleted successfully")
    return redirect('all_employee')

def allEmployee(request):
    context={}
    employees=Employee.objects.all()
    context['employees']=employees
    return render(request,'admin/all_employee.html',context)