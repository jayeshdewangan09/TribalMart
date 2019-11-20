from django.contrib import admin
from .models import Registration, Vendor, Operator, Product, Product_request , Pulled_requests, CustomerQuery, Orders, OrderUpdate
# Register your models here.


admin.site.register(Product)
admin.site.register(Registration)
admin.site.register(Vendor)
admin.site.register(Operator)
admin.site.register(Product_request)
admin.site.register(Pulled_requests)
admin.site.register(CustomerQuery)
admin.site.register(Orders)
admin.site.register(OrderUpdate)

