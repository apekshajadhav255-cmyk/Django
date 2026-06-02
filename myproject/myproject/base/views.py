from django.shortcuts import render,redirect
from .models import Product

# Create your views here.
def home(request):

    #CREATE OPERATION
    # a = Product(name='bat',price=1500)
    # a.save()

    # Product.objects.create(name='iphone',price=80000)

    #READ OPERATION
    a = Product.objects.get(id=5)
    print(a)

    b = Product.objects.filter(name='bat')

    c = Product.objects.all()
    
    print(request.method)#GET
    print(request.GET)#<QueryDict: {}> <QueryDict: {'product_name': ['pen'], 'price': ['50']}>
    #GET METHOD
    #whenever we are trying to fetch something from the empty querydict it will throw MultiValueDictKeyError
    if 'product_name' in request.GET:
        name = request.GET['product_name']
        price = request.GET['price']
        print(name,price)#pen 50
        # a = Product(name=name,price=price)#fieldname=var_name
        # a.save()
        Product.objects.create(name=name,price=price)

    print(request.POST)#<QueryDict: {'csrfmiddlewaretoken': ['v5u1G5TESkEPaV30ghYrkSk3PHMAXQjmYlYbkbnusCpbN2oU9mS3CosVvUwXU64B'], 'product_name': ['cake'], 'price': ['120']}>
    if request.method == 'POST':
        name = request.POST['product_name']
        price = request.POST['price']
        print(name,price)#cake 120
        Product.objects.create(name=name,price=price)
    return render(request,'home.html',{'data':a,'data1':b,'data2':c})

#CSRF - Cross Site Request Forgery 
def update(request,pk):
    # data = Product.objects.get(id=1)
    # print(data.name,data.price)
    # data.name = 'ball'
    # data.price = 500
    # data.save()
    print(pk)
    data = Product.objects.get(id=pk)
    print(data)
    print(request.method)
    print(request.GET)
    print(request.POST)
    if request.method == 'POST':
        name=request.POST['product_name']
        price=request.POST['product_price']
        print(new_name,new_price)
        data.name = new_name
        data.price = new_price
        data.save()
        return redirect('home')
    return render(request,'update.html',{'data':data})




































































































