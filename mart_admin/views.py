from django.shortcuts import render
from .forms import ProductForm
# Create your views here.
def test(request):
    form=ProductForm(request.POST or None)
    return render(request,'test.html',{'form':form})
