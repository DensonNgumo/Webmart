from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from mart_admin.models import Product,Customer,Category


def addToCart(request,product_id):
    if not 'productList' in request.session or not request.session['productList']:
        request.session['productList']=[product_id]
    else:       
        productList=request.session['productList']
        productList.append(product_id)
        request.session['productList']=productList
             
    return HttpResponseRedirect(reverse('home'))

def loadCart(request):
    products=[]
    if 'productList' in request.session:
        productList=request.session['productList']
        for product_id in productList:
            product=Product.objects.get(pk=product_id)
            products.append(product)

  
    return render(request,'cart.html',{'products':products})

def removeFromCart(request,product_id):
    productList=request.session['productList']
    productList.remove(product_id)
    request.session['productList']=productList
    return HttpResponseRedirect(reverse('cart_items'))