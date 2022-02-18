from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
         name = request.POST['name']
         age = int(request.POST['age'])
         dob = request.POST['dob']
         email = request.POST['email']
         Mobile_No = request.POST['M_No']
         Enrollment_No = request.POST['E_No']
         object =Student(name = name,age=age,dob=dob,email=email, Mobile_No=Mobile_No,Enrollment_No=Enrollment_No)

         object.save()
    return render(request,'home.html')
