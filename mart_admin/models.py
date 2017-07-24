from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name=models.CharField(max_length=150)

    class Meta:
        verbose_name_plural="categories"

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name=models.CharField(max_length=150)
    description=models.TextField(default='Default product description')
    price=models.IntegerField()
    product_image=models.FileField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_quantity=models.IntegerField()

    def __str__(self):
        return self.product_name

class Customer(models.Model):
    user=models.ForeignKey(User,default=1)
    customer_name=models.CharField(max_length=150)
    customer_email=models.EmailField()
    customer_mobile_number=models.CharField(max_length=14)
    customer_address=models.CharField(max_length=250)

    def __str__(self):
        return self.customer_name
    

class PaymentDetails(models.Model):
    class Meta:
        verbose_name_plural ="paymentDetails"

    PAYMENT_METHODS=(
        ('debit','Debit Card'),
        ('mpesa','MPESA'),
        ('cash','Cash on Delivery'))
    customer=models.ForeignKey(Customer)
    total_products=models.IntegerField()
    total_price=models.IntegerField()
    order_date_time=models.DateTimeField(auto_now=True)
    payment_method=models.CharField(max_length=10,choices=PAYMENT_METHODS)

