from django.db import models
import uuid
import os
import datetime

def products_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('shop/products', filename)


def request_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('shop/requests', filename)

def pulledreq_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('shop/pulled', filename)


# Create your models here.








class Registration(models.Model):
    cust_fname= models.CharField(max_length=50)
    cust_lname= models.CharField(max_length=50)
    cust_dob= models.CharField(max_length=10)
    cust_email= models.EmailField(primary_key=True)
    cust_pass=models.CharField(max_length=50)
    cust_mobile=models.IntegerField()
    cust_gender=models.CharField(max_length=10)
    cust_address=models.CharField(max_length=300)
    cust_city=models.CharField(max_length=50)
    cust_pin=models.IntegerField()
    cust_state=models.CharField(max_length=30)
    cust_country=models.CharField(max_length=30)


    def __str__(self):
        return self.cust_email


class Vendor(models.Model):
    vendor_firmname= models.CharField(max_length=200)
    vendor_owner= models.CharField(max_length=50)
    vendor_email= models.EmailField(primary_key=True)
    vendor_pass=models.CharField(max_length=50)
    vendor_mobile=models.IntegerField()
    vendor_address=models.CharField(max_length=300)
    vendor_city=models.CharField(max_length=50)
    vendor_pin=models.IntegerField()
    vendor_state=models.CharField(max_length=30)
    vendor_country=models.CharField(max_length=30)


    def __str__(self):
        return self.vendor_firmname + "~~~" + self.vendor_email


class Operator(models.Model):
    operator_fname= models.CharField(max_length=50)
    operator_lname= models.CharField(max_length=50)
    operator_email= models.EmailField(primary_key=True)
    operator_pass=models.CharField(max_length=50)
    operator_mobile=models.IntegerField()
    operator_address=models.CharField(max_length=300)
    operator_city=models.CharField(max_length=50)
    operator_pin=models.IntegerField()
    operator_state=models.CharField(max_length=30)
    operator_country=models.CharField(max_length=30)


    def __str__(self):
        return self.operator_fname + "~~~" + self.operator_email



class Product(models.Model):
    product_id= models.CharField(max_length=50, primary_key=True,default=datetime.datetime.now())
    product_name= models.CharField(max_length=50)
    category= models.CharField(default='', max_length=50)
    subcategory= models.CharField(max_length=50, default='')
    price= models.IntegerField(default=0)
    desc=models.CharField(max_length=300, default='')
    pub_date=models.CharField(max_length=50, default=datetime.datetime.now())
    image=models.ImageField(upload_to=products_path, default='2')

    def __str__(self):
        return self.product_name



class Product_request(models.Model):
    request_id = models.CharField(max_length=50, primary_key=True, default=datetime.datetime.now())
    product_name= models.CharField(max_length=50)
    category= models.CharField(max_length=50)
    subcategory= models.CharField(max_length=50)
    price= models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.CharField(max_length=50, default=datetime.datetime.now())
    image=models.ImageField(upload_to=request_path)
    vendor_firmname = models.CharField(max_length=200)
    vendor_email = models.EmailField()

    def __str__(self):
        return self.product_name + " ~~Raised by~~ " + self.vendor_firmname


class Pulled_requests(models.Model):
    product_id=models.CharField(max_length=50, primary_key=True, default=datetime.datetime.now())
    oldproduct_name=models.CharField(max_length=200)
    newproduct_name=models.CharField(max_length=200)
    oldcategory = models.CharField(max_length=50)
    newcategory = models.CharField(max_length=50)
    old_subcategory = models.CharField(max_length=50)
    new_subcategory = models.CharField(max_length=50)
    olddesc = models.CharField(max_length=300)
    newdesc = models.CharField(max_length=300)
    request_date = models.CharField(max_length=20)
    pulled_date = models.CharField(max_length=20)
    requestedby_vendor = models.CharField(max_length=200)
    requestedby_email = models.EmailField()
    pulledby_operator = models.CharField(max_length=200)
    pulledby_email = models.EmailField()
    image = models.ImageField(upload_to=products_path)
    oldprice = models.IntegerField(default=0)
    newprice = models.IntegerField(default=0)


    def __str__(self):
        return self.newproduct_name + " ~~Pulled by~~ " + self.pulledby_operator


class CustomerQuery(models.Model):
    query_id = models.CharField(max_length=50, primary_key=True, default=datetime.datetime.now())
    cust_email= models.EmailField()
    query = models.CharField(max_length=1000)
    query_date = models.CharField(max_length=50)
    query_time = models.CharField(max_length=50)

    def __str__(self):
        return self.query_id + "     Query by     " + self.cust_email


class Orders(models.Model):
    order_id = models.CharField(max_length=50, primary_key=True, default=datetime.datetime.now())
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    cust_name = models.CharField(max_length=80)
    cust_email = models.EmailField()
    cust_phone = models.CharField(max_length=15,default='')
    cust_pin = models.CharField(max_length=7,default='')
    address1 = models.CharField(max_length=200, default='')
    address2 = models.CharField(max_length=200, default='')
    address3 = models.CharField(max_length=200, default='')
    town_city = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    address_type = models.CharField(max_length=100)

    def __str__(self):
        return self.order_id + "     Order by     " + self.cust_email



class OrderUpdate(models.Model):
    update_id  = models.CharField(max_length=50, primary_key=True,default=datetime.datetime.now())
    order_id = models.CharField(max_length=50, default="")
    update_desc = models.CharField(max_length=5000)
    operator_email = models.CharField(max_length=100,default="Order placement")
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "...  of order -  " + self.order_id