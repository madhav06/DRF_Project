from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def home(request):
    managers = Manager.objects.all()
    staffs = Staff.objects.all()

    return render(request, 'accounts/dashboard.html', {'managers': managers, 'staffs': staffs })

def login(request):
    return render(request, 'accounts/login.html')

def signup(request):
    return render(request, 'accounts/signup.html')

def manager(request):
    managers = Manager.objects.all()
    return render(request, 'accounts/manager.html', {'managers': managers})

def staff(request):
    staffs = Staff.objects.all()

    return render(request, 'accounts/staff.html', {'staffs': staffs})


def utility(request):
    return render(request, 'accounts/utility.html')
