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


