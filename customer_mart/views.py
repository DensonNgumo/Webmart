from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,HttpResponseRedirect
from django import template
from django.forms.models import model_to_dict
from django.urls import reverse
from mart_admin.models import Product,Customer,Category

register=template.Library()

@register.simple_tag
def get_obj(pk,attr):
    obj=getattr(Product.objects.get(pk=int(pk)),attr)
    return obj

def index(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    return render(request,'customer_mart/index.html',{'products':products,'categories':categories})

def productsByCategory(request,category_id):
    #category=Category.objects.get(id=category_id)
    categories=Category.objects.all()
    products=Product.objects.select_related().filter(category=category_id)
    return render(request,'customer_mart/index.html',{'products':products,'categories':categories})

def addToCart(request,product_id):
    if not 'productList' in request.session or not request.session['productList']:
        request.session['productList']=[product_id]
    else:       
        productList=request.session['productList']
        productList.append(product_id)
        request.session['productList']=productList
             
    return HttpResponseRedirect(reverse('home'))

def test(request):
    products=[]
    if 'productList' in request.session:
        productList=request.session['productList']
        for product_id in productList:
            product=Product.objects.get(pk=product_id)
            products.append(product)

  
    return render(request,'customer_mart/test.html',{'products':products})
    
   