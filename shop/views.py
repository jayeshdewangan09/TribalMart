from django.shortcuts import render, redirect
from datetime import date
from math import ceil
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
from django.contrib.auth.models import auth, User
from django.contrib.auth import login, logout, authenticate
# Create your views here.
from django.http import HttpResponse
import datetime
from django.db import IntegrityError, transaction
from .models import Registration, Product, Vendor, Operator, Product_request, Pulled_requests, CustomerQuery, Orders, OrderUpdate
import os.path
import uuid
import json
MERCHANT_KEY = 'WVyQ80J9C@R!xFMw'

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)


def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query) < 4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)


def signup(request):
    if request.method == 'POST':

        c_fname = request.POST.get('First_Name', '')
        c_lname = request.POST.get('Last_Name', '')
        c_dob_day = request.POST.get('Birthday_day', '')
        c_dob_month = request.POST.get('Birthday_Month', '')
        c_dob_year = request.POST.get('Birthday_Year', '')
        c_email = request.POST.get('Email_Id', '')
        c_pass = request.POST.get('Password', '')
        c_mobile = request.POST.get('Mobile_Number', '')
        c_gender = request.POST.get('Gender', '')
        c_address = request.POST.get('Address', '')
        c_city = request.POST.get('City', '')
        c_pin = request.POST.get('Pin_Code', '')
        c_state = request.POST.get('State', '')
        c_country= request.POST.get('Country', '')

        final_dob= c_dob_day + c_dob_month + c_dob_year;
        registration = Registration(cust_fname=c_fname, cust_lname=c_lname, cust_dob=final_dob, cust_email=c_email,
                                    cust_pass=c_pass, cust_mobile=c_mobile, cust_gender=c_gender,
                                    cust_address=c_address, cust_city=c_city, cust_pin=c_pin, cust_state=c_state,
                                    cust_country=c_country)
        registration.save()
    return render(request, 'shop/signup.html')


def login(request):
    if request.method == 'POST':
        utype = request.POST.get('user_type', '')
        if utype == "vendor":
            username = request.POST.get('admin_id', '')
            password = request.POST.get('admin_password', '')
            try:
                obj = Vendor.objects.get(vendor_email=username)
                user_data = {'user_email': obj.vendor_email,
                             'user_pass': obj.vendor_pass,
                             'user_name':obj.vendor_firmname}
                if password == user_data['user_pass']:
                    return render(request, 'shop/vendor_request.html',user_data)
                else:
                    return render(request, 'shop/login.html', {'Password_match': False})
            except:
                return render(request, 'shop/login.html',{'found': False})

        elif utype == "operator":
            username = request.POST.get('admin_id', '')
            password = request.POST.get('admin_password', '')
            try:
                obj1 = Operator.objects.get(operator_email=username)

                obj2= Product_request.objects.values_list('request_id', 'product_name', 'category', 'subcategory',
                                                          'price', 'desc', 'pub_date', 'image', 'vendor_firmname',
                                                          'vendor_email')
                user_data = {'user_email': obj1.operator_email,
                             'user_pass': obj1.operator_pass,
                             'user_fname': obj1.operator_fname,
                             'user_name': str(obj1.operator_fname)+" "+ str(obj1.operator_lname)
                             ,'request_details' : obj2}
                for i in range(len(user_data['request_details'])):
                    for j in range(len(user_data['request_details'][i])):
                        print((user_data['request_details'][i])[j]);


                if password == user_data['user_pass']:
                    return render(request, 'shop/request_list.html', user_data)
                else:
                    return render(request, 'shop/login.html', {'Password_match': False})
            except:
                return render(request, 'shop/login.html',{'found': False})
        else:
            try:
                username = request.POST.get('userid', '')
                password = request.POST.get('password', '')
                obj= Registration.objects.get(cust_email= username)
                print(obj.cust_pass)
                user_data={'user_fname':obj.cust_fname, 'user_lname' : obj.cust_lname, 'user_email':obj.cust_email, 'user_pass': obj.cust_pass}
                if(password==user_data['user_pass']):
                    print("okk...matched")
                    allProds = []
                    catprods = Product.objects.values('category', 'product_id')
                    cats = {item['category'] for item in catprods}
                    for cat in cats:
                        prod = Product.objects.filter(category=cat)
                        n = len(prod)
                        nSlides = n // 4 + ceil((n / 4) - (n // 4))
                        allProds.append([prod, range(1, nSlides), nSlides])
                    params = {'allProds': allProds}
                    user_data.update(params)
                    return render(request, 'shop/index.html', user_data)
                else:
                    return render(request, 'shop/login.html', {'Password_match': False})
            except:
                return render(request, 'shop/login.html',{'found': False})
    else:
        return render(request, 'shop/login.html')


def ven_request(request):
    if request.method == 'POST':
        p_name = request.POST.get('product_name', '')
        p_category = request.POST.get('product_category', '')
        p_subcategory = request.POST.get('product_subcategory', '')
        p_price = request.POST.get('product_price', '')
        p_description = request.POST.get('product_description', '')
        p_date = request.POST.get('product_date', '')
        p_image = request.FILES.get('product_image', '')
        p_vendor = request.POST.get('vendor', '')
        p_vendoremail = request.POST.get('vendor_email', '')
        print(p_vendor,p_vendoremail)
        try:
            req= Product_request(request_id = datetime.datetime.now(), product_name = p_name, category=p_category,
                                 subcategory= p_subcategory, price= p_price, desc= p_description,
                                pub_date= p_date, image= p_image, vendor_firmname= p_vendor,
                                 vendor_email= p_vendoremail)
            req.save()
            user_data = {'user_email': p_vendoremail,
                         'user_name': p_vendor}

            return render(request, 'shop/vendor_request.html', user_data)
        except:
            return HttpResponse("Invalid form filled")
    else:
        return HttpResponse("form not filled")


@transaction.atomic
def request_list(request):
    if request.method == 'POST':
        oldp_id= request.POST.get('old_pro_id', '')
        oldp_name = request.POST.get('old_pro_name', '')
        oldp_category = request.POST.get('old_pro_category', '')
        oldp_subcategory = request.POST.get('old_pro_subcategory', '')
        oldp_price = request.POST.get('old_pro_price', '')
        oldp_description = request.POST.get('old_pro_desc', '')
        oldp_date = request.POST.get('old_pro_date', '')
        oldp_image = request.POST.get('old_pro_image', '')
        oldp_vendor = request.POST.get('old_pro_vendor', '')
        oldp_vendoremail = request.POST.get('old_pro_vendoremail', '')
        p_name = str(request.POST.get('pro_name', '')).strip()
        if p_name == '':
            p_name = str(oldp_name)
        p_category = request.POST.get('pro_category', '')
        if p_category == '-1':
            p_category = oldp_category
        p_subcategory = str(request.POST.get('pro_subcategory', '')).strip()
        if p_subcategory == '':
            p_subcategory = oldp_subcategory
        p_price = str(request.POST.get('pro_price', '')).strip()
        if p_price == '':
            p_price = oldp_price
        p_description = str(request.POST.get('pro_desc', '')).strip()
        if p_description == '':
            p_description = str(oldp_description)
        p_date = str(request.POST.get('pro_date', '')).strip()
        if p_date == '':
            p_date = str(oldp_date)
        p_image = oldp_image
        p_operator = request.POST.get('pro_operator', '')
        p_operator_mail = request.POST.get('pro_operatoremail', '')
        try:
            with transaction.atomic():
                del_req  = Product_request.objects.select_for_update().get(request_id = oldp_id)
                del_req.delete()
                dt= datetime.datetime.now()
                pull_req = Pulled_requests(product_id= oldp_id,
                    oldproduct_name= oldp_name,
                    newproduct_name= p_name,
                    oldcategory = oldp_category,
                    newcategory = p_category,
                    old_subcategory= oldp_subcategory,
                    new_subcategory= p_subcategory,
                    olddesc= oldp_description,
                    newdesc= p_description,
                    request_date= oldp_date,
                    pulled_date = dt.year + dt.month + dt.day,
                    requestedby_vendor= oldp_vendor,
                    requestedby_email= oldp_vendoremail,
                    pulledby_operator= p_operator,
                    pulledby_email= p_operator_mail,
                    image = p_image,
                    oldprice = oldp_price,
                    newprice = p_price)
                pull_req.save()
                obj1 = Operator.objects.get(operator_email=p_operator_mail)

                obj2 = Product_request.objects.values_list('request_id', 'product_name', 'category', 'subcategory',
                                                           'price', 'desc', 'pub_date', 'image', 'vendor_firmname',
                                                           'vendor_email')

                product_save= Product(product_id=oldp_id,product_name=p_name,category=p_category,
                                      subcategory= p_subcategory,price= p_price,desc=p_description,
                                      pub_date=dt.year + dt.month + dt.day, image= p_image)

                product_save.save()
                print("done till now...")

                user_data = {'user_email': obj1.operator_email,
                             'user_pass': obj1.operator_pass,
                             'user_name': str(obj1.operator_fname) + str(obj1.operator_lname),
                             'request_details': obj2}
                return render(request, 'shop/request_list.html', user_data)
        except Exception as e:
            print(e)
    else:
        return render(request, 'shop/request_list.html', '')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        query = request.POST.get('ntet', '')
        other_query = request.POST.get('qtype0', '')
        if query == '':
            query= other_query
        username = request.POST.get('userid', '')
        userfname = request.POST.get('userfname', '')
        now= datetime.datetime.now()
        current_date = now.strftime("%d/%m/%Y")
        current_time = now.strftime("%H:%M:%S")
        user_data = {'user_email': username, 'user_fname': userfname, 'ind': False}
        try:
            query_req = CustomerQuery(query_id = now , cust_email= username, query = query , query_date = current_date , query_time =current_time)
            query_req.save()
            print("saved")
            user_data['ind'] = True
            return render(request, 'shop/contact.html', user_data)

        except Exception as e:
            print("No data saved...",e)
            return render(request, 'shop/contact.html', user_data)
    else:
        print("There is an Error...")
        return render(request, 'shop/contact.html')


def contact_login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('userid', '')
            password = request.POST.get('password', '')
            obj = Registration.objects.get(cust_email=username)
            print(obj.cust_pass)
            user_data = {'user_fname': obj.cust_fname, 'user_lname': obj.cust_lname, 'user_email': obj.cust_email,
                         'user_pass': obj.cust_pass}
            if (password == user_data['user_pass']):
                print("okk...matched")
                print(username)
                return render(request, 'shop/contact.html', user_data)

            else:
                print("Password not matched")
        except Exception as e:
            print(e)
    else:
        print("Pass the user details..")


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, cust_email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
    return render(request, 'shop/tracker.html')





def operator_tracker(request):
    if request.method == 'POST':
        order_id = request.POST.get('orderId', '')
        update_desc = request.POST.get('desc', '')
        operator_email = request.POST.get('uem', '')
        try:
            obj = Orders.objects.filter(order_id=order_id)
            if len(obj)>0:
                now = datetime.datetime.now()
                obj1 = OrderUpdate(update_id = now, order_id = order_id, update_desc = update_desc, operator_email = operator_email)
                obj1.save()
                return render(request, 'shop/operator_tracker.html', {'order_id_not_found': False, 'update_id' : str(now)})
            else:
                return render(request, 'shop/operator_tracker.html',{'order_id_not_found' : True})
        except Exception as e:
            return render(request, 'shop/operator_tracker.html', {'order_id_not_found': True})
    else:
        return render(request, 'shop/operator_tracker.html')


def productView(request, myid):
    #fetch the products using the Id
    product = Product.objects.filter(product_id= myid)
    return render(request, 'shop/prodView.html',{'product': product[0]})


def checkout(request):
    if request.method == 'POST':
        now = str(uuid.uuid1())
        itemsJson = request.POST.get('itemsJson', '')
        cust_name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        cust_email = request.POST.get('user_email', '')
        cust_phone = request.POST.get('phone', '')
        cust_pin = request.POST.get('zip_code', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        address3 = request.POST.get('address3', '')
        town_city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        address_type = request.POST.get('addresstype', '')
        print(now, itemsJson,cust_name,cust_email,cust_phone,cust_pin,address1,address2,address3,town_city,state,address_type)
        try:
            order = Orders(order_id = now, items_json=itemsJson, cust_name= cust_name, cust_email= cust_email,
                           cust_phone= cust_phone, cust_pin = cust_pin, address1 = address1, address2 = address2,
                           address3 = address3, town_city= town_city, state = state, address_type = address_type, amount=amount)
            order.save()
            thank = True
            update = OrderUpdate(update_id = now, order_id=now, update_desc="The order has been placed")
            update.save()
            id = str(now)
            #return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
            # Request paytm to transfer the amount to your account after payment by user
            param_dict = {

                'MID': 'zSMafn07580070778962',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': cust_email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL': 'http://127.0.0.1:8000/shop/handlerequest/',

            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'shop/paytm.html', {'param_dict': param_dict})
        except Exception as e:
            thank = False
            print(e)
            print("Not saved..")
            return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    else:
        return render(request, 'shop/checkout.html')



def checkout_login(request):
    if request.method == 'POST':
        username = request.POST.get('userid', '')
        password = request.POST.get('password', '')
        try:
            obj = Registration.objects.get(cust_email=username)
            user_data = {'user_fname': obj.cust_fname, 'user_lname': obj.cust_lname, 'user_email': obj.cust_email,
                         'user_pass': obj.cust_pass}
            if password == user_data['user_pass']:
                print("matched")
                return render(request, 'shop/checkout.html', user_data)

            else:
                checking = False
                print("Password not matched")
                return render(request, 'shop/checkout.html', {'checking': checking})
        except Exception as e:
            print(e)
            checking_email = False
            return render(request, 'shop/checkout.html', {'checking_email': checking_email})
    else:
        print("Pass the user details..")

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
            print(response_dict['RESPCODE'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})
    # return HttpResponse('done')
    # pass


