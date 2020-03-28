from django.shortcuts import render
import json
from math import ceil
from django.http import HttpResponse
from .models import Products,Orders,Contact,Order_update
def index(request):
    allProds = []
    catprods = Products.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Products.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(0, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request,'coffee/index.html',params)
def about(request):
    return render(request,'coffee/about.html')
def contact(request):
    thank=False
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank=True

    return render(request,'coffee/contact.html',{'thank':thank})
def track(request):
    if request.method=="POST":
        orderId=request.POST.get('orderid','')
        email=request.POST.get('email','')
        try:
            order=Orders.objects.filter(order_id=orderId,email=email)
            if(len(order)>0):
                update=Order_update.objects.filter(orderId=orderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps([updates,order[0].item_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,'coffee/track.html')
def Login(request):
    return render(request,'coffee/login.html')
def Sign_up(request):
    return render(request,'coffee/signup.html')
def check_out(request):
    
    if request.method=="POST":
        item_json=request.POST.get('itemJson','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address1=request.POST.get('address1','')
        address2=request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip','')
        phone=request.POST.get('phone','')
        
        Order=Orders(item_json=item_json,name=name,email=email,phone=phone,address1=address1,address2=address2,city=city,state=state,zip_code=zip_code)
        Order.save()
        update=Order_update(order_id=Order.order_id,update_desc="Your order has been placed successfully....")
        update.save()
        thank=True
        id1=Order.order_id
        return render(request, 'coffee/checkout.html', {'thank':thank, 'id': id1})
    return render(request,'coffee/checkout.html')
def product(request,myid):
    # Fetch the product using id
    products1=Products.objects.filter(id=myid)
    return render(request,'coffee/product.html',{'pr':products1[0]})