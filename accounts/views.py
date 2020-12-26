from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import StaffForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
    managers = Manager.objects.all()
    staffs = Staff.objects.all()
    # utils = utility.objects.all()

    total_staffs = staffs.count()
    working_staffs = staffs.filter(status='IsActive').count()
    removed_staffs = staffs.filter(status='IsNotActive').count()

    return render(request, 'accounts/dashboard.html', {'managers': managers, 'staffs': staffs,  'total_staffs': total_staffs, 'working_staffs': working_staffs, 'removed_staffs': removed_staffs })

def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def manager(request):
    managers = Manager.objects.all()
    return render(request, 'accounts/manager.html', {'managers': managers})

def staff(request):
    # staffs = Staff.objects.get(id=pk_test)
    staffs = Staff.objects.all()

    # utils = staffs.category_set.all()

    context = {'staffs': staffs, }

    return render(request, 'accounts/staff.html', context)


def utility(request):
    return render(request, 'accounts/utility.html')


def addStaff(request):
    form = StaffForm()
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/staff_form.html')
