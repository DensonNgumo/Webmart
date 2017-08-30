from django import forms
from django.contrib.auth.models import User
from mart_admin.models import Customer

class CustomerForm(forms.ModelForm):
    customer_name=forms.CharField(required=True,help_text='Enter full name')
    class Meta:
        model=Customer
        fields=['customer_name','customer_email','customer_mobile_number','customer_address']