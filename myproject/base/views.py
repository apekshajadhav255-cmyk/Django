<<<<<<< HEAD
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
    data = TaskModel.objects.all()
    return render(request,'home.html',{'data':data})

def add(request):
    print(request.method)#GET #POST
    print(request.GET)#<QueryDict: {}>
    print(request.POST)#<QueryDict: {'csrfmiddlewaretoken': ['0H2qP0tU131tRt8h9SBNHpSpFkPzJPXVtXwAt6XKBlMPuAtb2XvpZV0hlxzWG5Ia'], 'title': ['django'], 'desc': ['need to work on model']}>
    if request.method == 'POST':
        title_data = request.POST['title']
        desc_data = request.POST['desc']
        print(title_data,desc_data)#django need to work on model
        TaskModel.objects.create(
            title = title_data,
            desc = desc_data
        )
        return redirect('home')
    return render(request,'add.html')

def complete(request):#task that has be completed need to be displayed
    data = CompleteModel.objects.all()
    return render(request,'complete.html',{'data':data})

def trash(request):
    data = TrashModel.objects.all()
    return render(request,'trash.html',{'data':data})

def about(request):
    return render(request,'about.html')

#HOME PAGE COMPLETE BUTTON
#1.Fetch the particular task from TaskModel - get method
#2. Create it in completemodel
#3.delete it from TaskModel
def completeh(request,id):
    data = TaskModel.objects.get(id=id)#fieldname=varname
    print(data)#object instance
    CompleteModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()
    return redirect('complete')

#home page delete button
def deleteh(request,id):
    data = TaskModel.objects.get(id=id)
    TrashModel.objects.create(
        title = data.title,
        desc = data.desc
    )
    data.delete()
    return redirect('trash')

#home page complete all button
def complete_allh(request):
    data = TaskModel.objects.all()
    #all return queryset
    for i in data:
        print(i)#each object instance
        CompleteModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        i.delete()
    return redirect('complete')

def update(request,id):
    data = TaskModel.objects.get(id=id)
    print(request.method)#GET #POST
    print(request.POST)#<QueryDict: {'csrfmiddlewaretoken': ['LosSxwhoFZHbFqwX67RztWOhELpBgcgJeEW2bCLefhsxixRRZcLbLsW9kY9Yds1Y'], 'title': ['django'], 'desc': ['need to work on todo project']}>
    if request.method == 'POST':
        title_data = request.POST['title']
        desc_data = request.POST['desc']
        print(title_data,desc_data)#django need to work on todo project
        print(data)
        data.title = title_data
        data.desc = desc_data
        data.save()
        return redirect('home')
    return render(request,'update.html',{'data':data})

#complete page restore button
#1. get the record from CompleteModel
#2. creted it in taskModel
#3.delete it from CompleteModel
def restore_c(request,id):
    data = CompleteModel.objects.get(id=id)
    TaskModel.objects.create(
        title=data.title,
        desc=data.desc
    )
    data.delete()
    return redirect('home')

#complete page restore all
#1. get all the record from CompleteModel
#2. creted it in taskModel one after the other
#3.delete it from CompleteModel
def restore_allc(request):
    data = CompleteModel.objects.all()
    print(data)#Queryset
    for i in data:
        print(i)#single object instance
        TaskModel.objects.create(
            title = i.title,
            desc = i.desc
        )
        # i.delete()#delete that particular record
    data.delete()#delete all records from CompleteModel
    return redirect('home')

#TRASH PAGE RESTORE
#1.get the record from TrashModel
#2. create it in TaskModel
#3.delete it from TrashModel
=======
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.db.models import Q

# Create your views here.
def home(request):
    print(request.method)#GET #GET(form method is GET)
    print(request.GET)#<QueryDict: {}> #<QueryDict: {'search': ['django']}>
    #fetch data entered in the search bar
    if 'search' in request.GET:
        q = request.GET['search']
        print(q)#django
        data = Student.objects.filter( Q(name__icontains = q) | Q(course__icontains = q))
        if not data.exists():#exists will check queryset empty or not if data is present in it it will return True else False when it is returning false with the help not operator i am making it True
            return HttpResponse('RECORD NOT FOUND')
    else:
        data = Student.objects.all()
    return render(request,'home.html',{'data':data})

def add(request):
    if request.method == 'POST':
        # name = request.POST['sname']
        # course = request.POST['course']
        Student.objects.create(
            name = request.POST['sname'],
            course = request.POST['course']
        )
    return render(request,'add.html')

#create operation through the views
#i want filter out the records based more than on 1 condition
'''
LOGICAL OPERATOR
OR - |
AND - &
NOT - ~

Q Class - Q is class provided by django that allows us to build the complex database queries using logical operator

using Q class u need convert condition to query expression object

field lookup  __icontains
if will check if the field contains the value coming from the frontend, ignoring case
field_name__icontains
'''


>>>>>>> f8dba96501fb03a42c59f7c82ad17de050d38c26
