from django.shortcuts import render
from mart_admin.models import Product,Customer,Category


def index(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    return render(request,'customer_mart/index.html',{'products':products,'categories':categories})

def productsByCategory(request,category_id):
    #category=Category.objects.get(id=category_id)
    categories=Category.objects.all()
    products=Product.objects.select_related().filter(category=category_id)
    return render(request,'customer_mart/index.html',{'products':products,'categories':categories})