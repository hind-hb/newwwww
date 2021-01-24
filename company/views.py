from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth import login as auth_login
from .form import *
from django.utils import timezone


# Create your views here.


def home(request):
    return render(request,'base.html')


def index(request):
    return render(request,'index.html')


def blockchain(request):
    return render(request,'new.html')


def employee(request):
    obj=Employee.objects.all()
    myform=NewEmp(request.POST)
    return render(request,'employee.html',{'obj':obj},{'myform':NewEmp})


def department(request):
    dept=Department.objects.all()
    return render(request,'department.html',{'dept':dept})


@login_required
def signup(request):
    if request.method=='POST':
        form =signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('home')
    else :
       form = signUpForm()
    return render (request,'signup.html',{'form':form})













