from calculator.models import Person
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
        if request.method == 'POST':
                name1 = request.POST['name']
                age1 = int(request.POST['age'])
                dob1 = request.POST['dob']
                email1 = request.POST['email']
                object =Person(name = name1,age=age1,dob=dob1,email=email1)

                object.save() 
        return render(request,'home.html')
    
# def calculate(request):
#     if request.POST['add']:
#         num1 = int(request.POST['num1'])
#         num2 = int(request.POST['num2'])
#         ans = num1 + num2
    

#     return render(request,'result.html',{'result':ans})


# def add(request):
#         num1 = int(request.POST['num1'])
#         num2 = int(request.POST['num2'])
#         ans = num1 + num2
#         return render(request,'result.html',{'result':ans})
    
# def sub(request):
#         num1 = int(request.POST['num1'])
#         num2 = int(request.POST['num2'])
#         ans = num1 - num2
#         return render(request,'result.html',{'result':ans})
    
# def multi(request):
#         num1 = int(request.POST['num1'])
#         num2 = int(request.POST['num2'])
#         ans = num1 * num2
#         return render(request,'result.html',{'result':ans})
    
# def div(request):
#         num1 = int(request.POST['num1'])
#         num2 = int(request.POST['num2'])
#         ans = num1/num2
#         return render(request,'result.html',{'result':ans})
    