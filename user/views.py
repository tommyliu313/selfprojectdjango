from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
#from user.models import User
from django.contrib.auth.models import User
from transfer.models import Transfer
from django.contrib import auth

# Create your views here.

# return to dashboard, show his information and record
def dashboard(request):
    return render(request, 'user/dashboard.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            user = User
    else:
        return render(request, 'user/login.html')

def logout(request):
    return render(request, 'user/redirect.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
    else:
        return render(request, 'user/register.html')