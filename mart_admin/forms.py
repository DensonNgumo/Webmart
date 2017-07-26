from django import forms
from .models import Category,Customer,Product,PaymentDetails


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['category_name']

class ProductForm(forms.ModelForm):
    category=forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model=Product
        fields=['product_name','description','price','category','product_image','product_quantity']

    
    
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['customer_name','customer_email','customer_mobile_number','customer_address']

class PaymentDetailsForm(forms.ModelForm):

    class Meta:
        model=PaymentDetails
        fields=['payment_method']