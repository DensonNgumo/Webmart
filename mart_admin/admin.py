from django.contrib import admin

from .models import Category,Product,Customer,PaymentDetails,StockDetails

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(PaymentDetails)
admin.site.register(StockDetails)