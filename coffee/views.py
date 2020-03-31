from django.shortcuts import render
import json
from math import ceil
from django.http import HttpResponse
from .models import Products, Orders, Contact, Order_update
from django.views.decorators.csrf import csrf_exempt
from . import checksum

MERCHANT_KEY = "3rcCVGv2DCExfX42"


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():

        return True
    else:
        return False


def index(request):
    
    allProds = []
    catprods = Products.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Products.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(0, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'coffee/index.html', params)


def search(request):
    query = request.GET.get('search','')
    allProds = []
    catprods = Products.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        
        prodtemp = Products.objects.filter(category=cat)
        prod = []
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if(n!=0):
            allProds.append([prod, range(0, nSlides), nSlides])
    params = {'allProds': allProds,'msg':''}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'coffee/search.html', params)


def about(request):
    return render(request, 'coffee/about.html')


def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True

    return render(request, 'coffee/contact.html', {'thank': thank})


def track(request):
    if request.method == "POST":
        orderId = request.POST.get('orderid', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if(len(order) > 0):
                update = Order_update.objects.filter(orderId=orderId)
                updates = []
                for item in update:
                    updates.append(
                        {'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(
                        {"status":"Success","Updates":updates, "itemJson":order[0].item_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"No item"}')
        except Exception as e:
            return HttpResponse('{"status":"Error"}')
    return render(request, 'coffee/track.html')


def Login(request):
    return render(request, 'coffee/login.html')


def Sign_up(request):
    return render(request, 'coffee/signup.html')


def check_out(request):

    if request.method == "POST":
        item_json = request.POST.get('itemJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', 0)
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')
        phone = request.POST.get('phone', '')

        Order = Orders(item_json=item_json, amount=amount, name=name, email=email, phone=phone,
                       address1=address1, address2=address2, city=city, state=state, zip_code=zip_code)
        Order.save()
        update = Order_update(
            orderId=Order.order_id, update_desc="Your order has been placed successfully....")
        update.save()
        thank = True
        id1 = Order.order_id
        # return render(request, 'coffee/checkout.html', {'thank':thank, 'id': id1})
        # return request to paytm to accept amount from user
        param_dict = {
            'MID': 'msOvtD83762450366770',
            'ORDER_ID': str(Order.order_id),
            'TXN_AMOUNT': str(Order.amount),
            'CUST_ID': str(Order.email),
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/coffee/handleRequest/',
        }
        param_dict['CHECKSUMHASH'] = checksum.generate_checksum(
            param_dict, MERCHANT_KEY)
        return render(request, 'coffee/paytm.html', {'param_dict': param_dict})
    return render(request, 'coffee/checkout.html')


def product(request, myid):
    # Fetch the product using id
    products1 = Products.objects.filter(id=myid)
    return render(request, 'coffee/product.html', {'pr': products1[0]})


@csrf_exempt
def handleRequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum1 = form[i]
    verify = checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum1)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' +
                  response_dict['RESPMSG'])
    return render(request, 'coffee/paymentstatus.html', {'response': response_dict})
