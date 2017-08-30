from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from mart_admin.models import Product,Customer,Category
from .forms import CustomerForm


def index(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    return render(request,'customer_mart/index.html',{'products':products,'categories':categories})

def productsByCategory(request,category_id):
    categories=Category.objects.all()
    products=Product.objects.select_related().filter(category=category_id)
    return render(request,'customer_mart/index.html',{'products':products,'categories':categories})


def details(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request,'customer_mart/details.html',{'product':product})

@login_required
def editProfile(request):
    form=CustomerForm(request.POST or None)
    if form.is_valid():
        customer=form.save(commit=False)
        customer.user=request.user
        customer.customer_name=form.cleaned_data['customer_name']
        customer.customer_email=form.cleaned_data['customer_email']
        customer.customer_mobile_number=form.cleaned_data['customer_mobile_number']
        customer.customer_address=form.cleaned_data['customer_address']
        customer.save()
        form=None

    return render(request,'customer_mart/profile.html',{'form':form})

   