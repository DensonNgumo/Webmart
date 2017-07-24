from django.shortcuts import render
from .forms import ProductForm,CategoryForm
# Create your views here.

def addProducts(request):
    form=ProductForm(request.POST or None,request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        product=form.save(commit=True)
        product.save()
        return render(request,'mart_admin/add_products.html',{'form':form})
    else:
        return render(request,'mart_admin/add_products.html',{'form':form})


def addCategories(request):
    form=CategoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()       
        return render(request,'mart_admin/add_categories.html',{'form':form})
    else:
        return render(request,'mart_admin/add_categories.html',{'form':form})