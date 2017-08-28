from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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

@login_required
def proceedToCheckout(request):
    products=[]
    total=0
    if 'productList' in request.session:
        productList=request.session['productList']
        for product_id in productList:
            product=Product.objects.get(pk=product_id)
            products.append(product)
        for product in products:
            total+=product.price

    return render(request,'checkout.html',{'products':products,'total':total})

    


@login_required
def checkout(request):
    stock=0
    if 'productList' in request.session:
        productList=request.session['productList']
        for product_id in productList:
            product=Product.objects.get(pk=product_id)
            if(product.product_quantity>=1):
                product.product_quantity=product.product_quantity-1
                product.save()
                stock=product.product_quantity
        message="Purchase made,await confirmation email"
        del request.session['productList']   
    
    return render(request,'checkout.html',{'message':message,'stock':stock})

def clearCart(request):
    isCheckedOut=request.GET.get('checkout_complete',None)
    if(isCheckedOut):
        data={'success':True}
        return JsonResponse(data)
    else:
        data={'success':False}
        return JsonResponse(data)

    
    